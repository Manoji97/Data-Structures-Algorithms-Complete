'''
Given a Set S

from the the given subsets find the subsets that can result to S un union
each element should be atmost 1 time
'''

'''
	1	2	3	4	5	6
A   1   1	0	0	0	0
B   1	1	1	0	0	0
C   0	0	0	1	1	0
D   0	0	1	0	0	1
E   0	0	0	0	0	1

this is represented Below

'''


import math

S = [1, 2, 3, 4, 5, 6]


subsets = {
	'A' : [1, 2, 6],
	'B' : [1, 2, 3],
	'C' : [4, 5],
	'D' : [3, 6],
	'E' : [6]
	}

subsets1 = {
	'A' : [1, 4, 7],
	'B' : [1, 4],
	'C' : [4, 5, 7],
	'D' : [3, 5, 6],
	'E' : [2, 3, 6, 7],
	'F' : [2, 7]
}


sd4x4 = {
	'p02-1': ['R01', 'C21', 'B11'],
	'p03-2': ['R02', 'C32', 'B12'],
	'p10-2': ['R12', 'C02', 'B02'],
	#'p23-4': ['R24', 'C34', 'B34'],
	'p30-4': ['R34', 'C04', 'B24'],
	'p31-3': ['R33', 'C13', 'B23'],

	'p23-4': ['R24', 'C34', 'B34'],
	'p23-3': ['R23', 'C33', 'B33'],
	'p23-1': ['R21', 'C31', 'B31'],

	'p00-1': ['R01', 'C01', 'B01'],
	'p00-3': ['R03', 'C03', 'B03'],
	'p01-4': ['R04', 'C14', 'B04'],
	'p11-1': ['R11', 'C11', 'B01'],
	'p11-4': ['R14', 'C14', 'B04'],
	'p12-3': ['R13', 'C23', 'B13'],
	'p12-4': ['R14', 'C24', 'B14'],
	'p13-3': ['R13', 'C33', 'B13'],
	'p20-1': ['R21', 'C01', 'B21'],
	'p21-1': ['R21', 'C11', 'B21'],
	'p21-2': ['R22', 'C12', 'B22'],
	'p22-2': ['R22', 'C22', 'B32'],
	'p22-3': ['R23', 'C23', 'B33'],
	'p32-2': ['R32', 'C22', 'B32'],
	'p33-1': ['R31', 'C31', 'B31'],
	
}



def createReduced(sub_sets, omit_subset, omit_constraint):
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


def getMinConstraint(look_up):
	min_constraint = None
	min_len = 1000
	for constraint in look_up:
		length = len(look_up[constraint])
		if length == 0: return False
		if min_len > length:
			min_len = length
			min_constraint = constraint


	return min_constraint

def deleteSubSets(look_up, constraints):
	delete_subsets = []
	for _constraint in constraints:
		for sub_set in look_up[_constraint]:
			if sub_set not in delete_subsets:
				delete_subsets.append(sub_set)
	return delete_subsets


def solve(sub_sets, covered_constraint = [], deleted_subset = [], final = []):
	r_subSet, r_lookUp = createReduced(sub_sets, deleted_subset, covered_constraint)
	#print(r_lookUp)

	if len(r_lookUp) == 0: 
		#print(sorted(final))
		return True
	#print(final)
	min_constraint = getMinConstraint(r_lookUp)
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

		delete = deleteSubSets(r_lookUp, r_subSet[_subset])

		for i in delete:
			if i not in deleted_subset:
				deleted_subset.append(i)

		#print("delete", deleted_subset)

		final.append(_subset)

		if solve(sub_sets, covered_constraint, deleted_subset, final):
			return True

		final.pop()
		#print("restored final", final)
		#print("restored cover",  covered_constraint[:ori_covered_constraint_len])
		covered_constraint = covered_constraint[:ori_covered_constraint_len]
		#print("restore delete", deleted_subset[: ori_delete_subset_len])
		deleted_subset = deleted_subset[: ori_delete_subset_len]

	return False



def getSubsets4x4(matrix):
	subsets_for_cover = {}

	rows = len(matrix)
	cols = len(matrix[0])

	for i in range(rows):
		for j in range(cols):
			val = matrix[i][j]
			if i < 2 and j < 2: B = 0
			elif i < 2 and j >= 2: B = 1
			elif i >= 2 and j < 2: B = 2
			elif i>= 2 and j >=2: B = 3 
			if val:
				key = f'p{i}{j}-{val}'
				value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
				subsets_for_cover[key] = value
			else:
				for val in range(1, 5):
					key = f'p{i}{j}-{val}'
					value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
					subsets_for_cover[key] = value

	return subsets_for_cover


def createSubsets9x9(matrix):
	length = len(matrix)

	subsets_for_cover = {}

	for i in range(length):
		for j in range(length):
			val = matrix[i][j]
			B = getBox(i, j)
			if val:
				key = f'p{i}{j}-{val}'
				value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
				subsets_for_cover[key] = value
			else:
				for val in range(1, 10):
					key = f'p{i}{j}-{val}'
					value = [f'p{i}{j}', f'R{i}{val}', f'C{j}{val}', f'B{B}{val}']
					subsets_for_cover[key] = value

	return subsets_for_cover



def getBox(i , j):
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
			



def createMatrix(rows, cols):
	A = [[ 0 for j in range(cols)] for i in range(rows)]
	return A


def printSudoku(matrix, lst):
	for i in lst:
		row = int(i[1])
		col = int(i[2])
		val = int(i[-1])
		matrix[row][col] = val
	for row in matrix:
		print(row)

	return matrix





#print(subsets_for_cover)



s = [[1, 0, 0, 0],
	 [0, 0, 1, 4],
	 [0, 1, 2, 0],
	 [0, 3, 0, 0]]

_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 3, 0, 8, 5],
		    [0, 0, 1, 0, 2, 0, 0, 0, 0],
		    [0, 0, 0, 5, 0, 7, 0, 0, 0],
		    [0, 0, 4, 0, 0, 0, 1, 0, 0],
		    [0, 9, 0, 0, 0, 0, 0, 0, 0],
		    [5, 0, 0, 0, 0, 0, 0, 7, 3],
		    [0, 0, 2, 0, 1, 0, 0, 0, 0],
		    [0, 0, 0, 0, 4, 0, 0, 0, 9]]


final = []
subsets4x4 = createSubsets9x9(_sudoku)
solution = solve(subsets4x4, final = final)

A = createMatrix(9, 9)
printSudoku(A, final)
#print(final)

