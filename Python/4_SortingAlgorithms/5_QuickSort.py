'''
Python Implementation of QuickSort

Time Complexity => O(n log n)

for detailed explaination refer JS implementation

'''

def Pivot(lst, start, end):
	ind = start
	current_val = lst[start]

	for i in range(start + 1, end):
		if lst[i] < current_val:
			ind += 1
			lst[ind], lst[i] = lst[i], lst[ind]

	lst[ind], lst[start] = lst[start], lst[ind]
	print(lst)
	return ind

def QuickSort(lst, start, end):
	if start < end:
		split_idx = Pivot(lst, start, end)

		QuickSort(lst,start, split_idx )
		QuickSort(lst, split_idx + 1, end)
	return lst
