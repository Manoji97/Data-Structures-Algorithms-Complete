def SumRange(num):
	if num == 0: return 0
	return num + SumRange(num -1)

def SumofDigits(num):
	if num/10 < 1: return num % 10
	s = num % 10
	num = int(num /10)
	return 	s + SumofDigits(num)