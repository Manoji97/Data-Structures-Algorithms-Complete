'''
Python Implementation of Insertion Sort

full details see JS implementation

Time Complexity is O(n^2)

'''

def InsertionSort(lst):
	lst_length = len(lst)

	for i in range(1, lst_length):
		current_idx = i
		for j in range(i-1, -1, -1):
			print(lst)
			if lst[j] <= lst[current_idx]: break
			lst[j],lst[current_idx] = lst[current_idx], lst[j]
			current_idx = j

	return lst


print(InsertionSort([6,3,1,56,8,5,78,4,0,45]))
