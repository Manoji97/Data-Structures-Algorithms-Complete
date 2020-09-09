'''
Input is a array holding both pos and neg numbers

find the largest continous Sum

'''

# Time Complexity is O(n)


def LargestContinousSum(lst):
	if len(lst) == 0: return 0

	max_sum = current_sum = lst[0]

	for i in lst[1:]:
		current_sum = max(i, current_sum + i)

		max_sum = max(max_sum, current_sum)
	return max_sum

print(LargestContinousSum([1, 2, -1, 3, 4, 10, 10, -10, -1]))