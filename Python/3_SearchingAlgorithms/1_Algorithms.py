import math

def LinearSearch(lst, elem):
	for i in range(len(lst)):
		if lst[i] == elem:
			return i
	return -1


# only sorted array
def BinarySearch(lst, elem):
	if elem < lst[0] or elem > lst[-1]: return -1
	left = 0
	right = len(lst)
	mid = math.floor((left + right)/2)

	while lst[mid] != elem:
		if left >= right: return -1

		if lst[mid] > elem:
			right = mid - 1
		elif lst[mid] < elem:
			left = mid +1

		mid = math.floor((left + right)/2)
	return mid

def NaiveStringSearch(long_str, short_str):
	long_len = len(long_str)
	short_len = len(short_str)

	count = 0

	for i in range(long_len - short_len + 1):
		if long_str[i: i+short_len] == short_str:
			count += 1
	return count 