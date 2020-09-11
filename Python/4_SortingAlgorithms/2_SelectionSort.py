'''
Selection Sort Python implementation

full reference refer JS implementation

Time Complexity => O(n^2)

basically waste

'''

def SelectionSort(lst):
	lst_length = len(lst)

	for i in range(lst_length):
		lowest_idx = i
		for j in range(i, lst_length):
			if lst[j] < lst[lowest_idx]:
				lowest_idx = j

		if lowest_idx != i:
			lst[i], lst[lowest_idx] = lst[lowest_idx], lst[i]
	return lst

print(SelectionSort([6,33,6,8,2,5,9,23,65,1]))

