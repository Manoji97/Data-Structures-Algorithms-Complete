'''
ex: pairSum([1, 3, 2, 2], 4)

output: (1, 3) and (2,2)

sum of Output should be equal to the number in input

'''

# For this method the Time Complexity is O(n)

def ArrayPairSum(lst, num):
	length = len(lst)
	if length < 2: return False

	seen = set()
	output = set()

	for i in lst:

		diff = num - i

		if diff not in seen:
			seen.add(i)
		else:
			output.add((min(i, diff), max(i, diff)))

	return output


print(ArrayPairSum([1,3,2,2], 4))