def SumRange(num):
	if num == 0: return 0
	return num + SumRange(num-1)

def Factorial(num):
	if num == 0: return 1
	return num * Factorial(num-1)

def GetAllOdds(lst, out = [], i=0):
	if i >= len(lst): return out

	if lst[i] % 2 != 0: out.append(lst[i])
	i += 1
	return GetAllOdds(lst, out, i)
	

def GetAllOdsPop(lst, out = []):
	if len(lst) == 0: return out
	val = lst.pop()
	if val %2 != 0: out.append(val)
	return GetAllOdds(lst, out)






	 