

def Fib_Basic(num):
	if num <= 2: return 1
	return Fib_Basic(num-1) + Fib_Basic(num-2)


# this takes more time than FIB_memo
def Fib_Memorisation(num):
	fib_dict = {
	1:1,
	2:1
	}

	def FIB(num):
		if num in fib_dict:
			return fib_dict[num]

		val = FIB(num - 1) + FIB(num - 2)
		fib_dict[num] = val
		return val
	return FIB(num)


def Fib_memo(num, memo = {1:1, 2:1}):
	if num in memo: return memo[num]

	memo[num] = Fib_memo(num-1, memo) + Fib_memo(num-2, memo)
	return memo[num]

def Fib_Tabular(num):
	fib_lst = [0, 1, 1]

	for i in range(3,num + 1):
		fib_lst.append(fib_lst[i-1] + fib_lst[i-2])
	return fib_lst[num]