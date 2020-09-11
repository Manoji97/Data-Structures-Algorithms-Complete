'''
refer JS implementation for Detail
'''


def MultiPointer(lst):
	left = 0
	right = len(lst) - 1

	while left < right:
		_sum = lst[left] + lst[right]

		if _sum == 0: break
		if _sum < 0: left +=1
		else: right -= 1

	return (left, right)
