'''
refer JS implementation for Detail explaination

'''


# lst is a sorted array
def CountUniqueNumbers(lst):
	if len(lst) == 0: return 0
	count = 1
	for i in range(1, len(lst)):
		if lst[i-1] != lst[i]:
			count += 1

	return count