import math
def getDigitAtIndex(num, digit):
	return math.floor(abs(num) / math.pow(10, digit)) % 10;

def getNumDigits(num):
	if num == 0: return 0
	return math.floor(math.log10(num)) + 1

def getMaxNumDigits(lst):
	max_digits = -1
	for i in lst:
		max_digits = max(max_digits, getNumDigits(i))
	return max_digits

def RadixSort(lst):
	max_digits = getMaxNumDigits(lst)

	for i in range(max_digits):
		BUCKETS = [[], [], [], [], [], [], [], [], [], []]
		for value in lst:
			BUCKETS[getDigitAtIndex(value, i)].append(value)

		lst = []
		for bucket in BUCKETS:
			lst += bucket

	return lst

		


