'''
This Sudoku solver uses Exact cover Problem's Algorithm

=> Algorithm X

but this doesnt uses Dancing links

we use dictionaries for this

'''

class SudokuSolver(object):
	def __init__(self, sudoku_matrix):
		self.board = sudoku_matrix
		self.rows = len(sudoku_matrix)
		self.cols = len(sudoku_matrix[0])

	def printBoard(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(f' {self.board[i][j]} ', end='')
				if (j+1)%3 == 0 and j+1 < self.cols: print(' | ', end= ' ')
			
			if (i+1)%3 == 0 and i+1 < self.rows: print('\n----------------------------------')
			else: print('\n')

	def checkBoardValidity(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.board[i][j] != 0:
					if not self.checkValidity(self.board[i][j], (i, j)): 
						return False
		return True


	def checkValidity(self, num, pos):
		# check in row
		for i in range(self.rows):
			#print(self.board[i][pos[1]], end = ' ')
			if pos[0] != i and self.board[i][pos[1]] == num:
				return False

		#print(' ')

		# check in col
		for i in range(self.cols):
			#print(self.board[pos[0]][i], end = ' ')
			if pos[1] != i and self.board[pos[0]][i] == num:
				return False

		#print(' ')

		part_row = int(pos[0]/3) *3
		part_col = int(pos[1]/3) *3
		#print(part_row, part_col)

		#check in the block
		for i in range(3):
			for j in range(3):
				#print(self.board[i+part_row][j+part_col], end = ' ')
				if (i+part_row, j+part_col) != pos and self.board[i+part_row][j+part_col] == num:
					return False
			#print('')

	

		#print(num, pos, True)
		return True


	def getBox(self, i , j):
		if i < 3 and j < 3: B = 0
		elif i < 3 and j >= 3 and j < 6: B=1
		elif i < 3 and j >= 6: B =2
		elif i >=3 and i < 6 and j < 3: B = 3
		elif i >=3 and i < 6 and j >=3 and j < 6: B = 4
		elif i >= 3 and i < 6 and j >=6: B = 5
		elif i >= 6 and j < 3: B = 6
		elif i >= 6 and j >=3 and j < 6: B = 7	
		elif i >= 6 and j >= 6: B = 8
		return B

	def createSubsets(self):
		length = len(self.board)

		subsets_for_cover = {}

		for i in range(length):
			for j in range(length):
				val = self.board[i][j]
				B = self.getBox(i, j)
				if val:
					key = f'p{i}{j}-{val}'
					value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
					subsets_for_cover[key] = value
				else:
					for val in range(1, 10):
						if self.checkValidity(val, (i, j)):
							key = f'p{i}{j}-{val}'
							value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
							subsets_for_cover[key] = value

		return subsets_for_cover

	def createReduced(self, sub_sets, omit_subset, omit_constraint):
		lookUp = {}

		for sub_set in sub_sets:
			for constraint in sub_sets[sub_set]:
				if constraint in omit_constraint: continue
				if constraint in lookUp: lookUp[constraint] += [sub_set]
				else: lookUp[constraint] = [sub_set]

		for sub_set in omit_subset:
			constraints = sub_sets[sub_set]
			for constraint in constraints:
				if constraint in lookUp:
					lookUp[constraint] = [i for i in lookUp[constraint] if i != sub_set]

		local_set = {}				
		for sub_set in sub_sets:
			if sub_set not in omit_subset:
				local_set[sub_set] = sub_sets[sub_set]


		return local_set,lookUp

	def getMinConstraint(self, look_up):
		min_constraint = None
		min_len = 1000
		for constraint in look_up:
			length = len(look_up[constraint])
			if length == 0: return False
			if min_len > length:
				min_len = length
				min_constraint = constraint


		return min_constraint

	def deleteSubSets(self, look_up, constraints):
		delete_subsets = []
		for _constraint in constraints:
			for sub_set in look_up[_constraint]:
				if sub_set not in delete_subsets:
					delete_subsets.append(sub_set)
		return delete_subsets

	def solve(self, sub_sets, covered_constraint = [], deleted_subset = [], final = []):
		r_subSet, r_lookUp = self.createReduced(sub_sets, deleted_subset, covered_constraint)
		#print(r_lookUp)

		if len(r_lookUp) == 0: 
			#print(sorted(final))
			return True
		#print(final)
		min_constraint = self.getMinConstraint(r_lookUp)
		#print("min",min_constraint)
		if not min_constraint: return False
		subsets = r_lookUp[min_constraint]

		ori_covered_constraint_len = len(covered_constraint)
		ori_delete_subset_len = len(deleted_subset)


		for _subset in subsets:
			#print("row", _subset)
			
			for constraint in r_subSet[_subset]:
				if constraint not in covered_constraint:
					covered_constraint.append(constraint)
			
			#print("covered", covered_constraint)

			delete = self.deleteSubSets(r_lookUp, r_subSet[_subset])

			for i in delete:
				if i not in deleted_subset:
					deleted_subset.append(i)

			#print("delete", deleted_subset)

			final.append(_subset)

			if self.solve(sub_sets, covered_constraint, deleted_subset, final):
				return True

			final.pop()
			#print("restored final", final)
			#print("restored cover",  covered_constraint[:ori_covered_constraint_len])
			covered_constraint = covered_constraint[:ori_covered_constraint_len]
			#print("restore delete", deleted_subset[: ori_delete_subset_len])
			deleted_subset = deleted_subset[: ori_delete_subset_len]

		return False

	def assignOutput(self, lst):
		for i in lst:
			row = int(i[1])
			col = int(i[2])
			val = int(i[-1])
			self.board[row][col] = val

		for row in self.board:
			print(row)


	def solveSudoku(self):
		final = []
		if self.checkBoardValidity():
			subset = self.createSubsets()
			if self.solve(subset, final = final):
				self.assignOutput(final)
			else: print("Cant Find!")
		else: print("In Valid Board")


_sudoku = [[0, 0, 0, 0, 0, 5, 0, 8, 0],
		   [0, 7, 9, 0, 0, 0, 0, 0, 6],
		   [0, 0, 0, 0, 4, 0, 0, 9, 2],
		   [0, 3, 0, 6, 0, 0, 0, 0, 0],
		   [2, 0, 4, 0, 0, 0, 1, 0, 8],
		   [0, 0, 0, 0, 0, 1, 0, 4, 0],
		   [6, 2, 0, 0, 3, 0, 0, 0, 0],
		   [4, 0, 0, 0, 0, 0, 8, 7, 0],
		   [0, 8, 0, 1, 0, 0, 0, 0, 0]]


sudoku = SudokuSolver(_sudoku)
sudoku.solveSudoku()