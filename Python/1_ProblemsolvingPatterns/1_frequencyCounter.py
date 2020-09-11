

def FrequencyCounter(lst1, lst2):
	if len(lst1) != len(lst2): return False

	lst1_dict = {}

	for i in lst1:
		if i in lst1_dict: lst1_dict[i] += 1
		else: lst1_dict[i] = 1

	for i in lst2:
		if i not in lst1_dict: return False
		if lst1_dict[i] == 0: return False
		else: lst1_dict[i] -= 1

	return True



