'''
Python Implementation for Merge Sort

Time Complexity  => O(n log n)

see JS implementation for detailed explaination
'''
import math

def Merge2SortedArray(lst1, lst2):
	out_lst = []

	idx = 0
	jdx = 0

	while idx < len(lst1) and jdx < len(lst2):
		if lst1[idx] < lst2[jdx]:
			out_lst.append(lst1[idx])
			idx += 1
		else:
			out_lst.append(lst2[jdx])
			jdx += 1

	while idx < len(lst1):
		out_lst.append(lst1[idx])
		idx += 1
	while jdx < len(lst2):
		out_lst.append(lst2[jdx])
		jdx += 1
	 	 
	return out_lst


def MergeSort(lst):
	if len(lst) == 1: return lst
	mid = math.floor(len(lst)/2)

	left = MergeSort(lst[:mid])
	right = MergeSort(lst[mid:])

	return Merge2SortedArray(left , right)
