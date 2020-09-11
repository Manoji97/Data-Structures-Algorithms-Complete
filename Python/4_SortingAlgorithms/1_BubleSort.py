'''

Bubble Sort Python Implementation
Time Complexity => O(n^2)

'''

def BubbleSort(lst):
	lst_length = len(lst)
	for i in range(lst_length):
		for j in range(lst_length - i -1):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
	return lst

BubbleSort([3,4,76,3,5,3,7,23,9,1])