'''

Sudoku Solver 
using back tracking

steps:
1) check if there is any empty slots
2) if not ur puzlle is solved
3) else pic the slot loop from 1 to 9, check for validity
4) if valid recurse to next emt slot
5) if no nums from 1 to 9 can solve that pos, recurse back and change and come back.

if ans return true, else false

but this not solving hard problems.

'''


class Sudoku(object):
	def __init__(self, sudoku_matrix):
		self.board = sudoku_matrix
		self.rows = 9
		self.cols = 9
		self.isCompleted = False

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
						print(i, j)
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

	def findSolution(self):
		if self.solve():
			self.printBoard()
		else: print(False)


	def findNextEmptyPos(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.board[i][j] == 0:
					return (i, j)

		return False

	def solve(self):
		# Base Condition
		pos = self.findNextEmptyPos()
		if not pos:
			return True
		self.printBoard()
		print(' ')

		for num in range(1, 10):
			if self.checkValidity(num, pos):
				self.board[pos[0]][pos[1]] = num
				if self.solve(): return True
				self.board[pos[0]][pos[1]] = 0

		return False

		
_sudoku = [[1, 0, 0, 4, 8, 9, 0, 7, 6],
		   [7, 3, 0, 0, 0, 0, 0, 4, 0],
		   [0, 0, 0, 0, 0, 1, 2, 9, 5],
		   [0, 0, 7, 1, 2, 0, 6, 0, 0],
		   [5, 0, 0, 7, 0, 3, 0, 0, 8],
		   [0, 0, 6, 0, 9, 5, 7, 0, 0],
		   [9, 1, 4, 6, 0, 0, 0, 0, 0],
		   [0, 2, 0, 0, 0, 0, 0, 3, 7],
		   [8, 0, 0, 5, 1, 2, 0, 0, 4]]

_sudoku2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 3, 0, 8, 5],
		    [0, 0, 1, 0, 2, 0, 0, 0, 0],
		    [0, 0, 0, 5, 0, 7, 0, 0, 0],
		    [0, 0, 4, 0, 0, 0, 1, 0, 0],
		    [0, 9, 0, 0, 0, 0, 0, 0, 0],
		    [5, 0, 0, 0, 0, 0, 0, 7, 3],
		    [0, 0, 2, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 0, 4, 0, 0, 0, 9]]

_sudoku3 = [[0, 0, 6, 0, 5, 4, 9, 0, 0],
		    [1, 0, 0, 0, 6, 0, 0, 4, 2],
		    [7, 0, 0, 0, 8, 9, 0, 0, 0],
		    [0, 7, 0, 0, 0, 5, 0, 8, 1],
		    [0, 5, 0, 3, 4, 0, 6, 0, 0],
		    [4, 0, 2, 0, 0, 0, 0, 0, 0],
		    [0, 3, 4, 0, 0, 0, 1, 0, 0],
		    [9, 0, 0, 8, 0, 0, 0, 5, 0],
		    [0, 0, 0, 4, 0, 0, 3, 0, 7]]

all_emt = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 3, 0, 8, 5],
			[0, 0, 1, 0, 2, 0, 0, 0, 0],
			[0, 0, 0, 5, 0, 7, 0, 0, 0],
			[0, 0, 4, 0, 0, 0, 1, 0, 0],
			[0, 9, 0, 0, 0, 0, 0, 0, 0],
			[5, 0, 0, 0, 0, 0, 0, 7, 3],
			[0, 0, 2, 0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 9]]


sudokuSolver = Sudoku(all_emt)

sudokuSolver.printBoard()

print('---------------Solution----------------')



if sudokuSolver.checkBoardValidity():
	sudokuSolver.findSolution()
else: print("Not a Valid board!")

