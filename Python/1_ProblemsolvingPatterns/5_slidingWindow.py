'''

input = [1,4,6,-6,7,-3,3,5,7], 4

find the max sum that 4 consecutive elems can add upto
'''
import math

def SlidingWindow(lst, num):
	temp_sum = sum(lst[:num])
	max_sum = temp_sum

	for i in range(num, len(lst)):
		temp_sum = temp_sum - lst[i -num] + lst[i]
		max_sum= max(max_sum, temp_sum)
	return max_sum