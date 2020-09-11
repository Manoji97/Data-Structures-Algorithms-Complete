def ChechAnagram(str1, str2):
	if len(str1) != len(str2): return False
	
	look_up = {}

	for i in str1:
		if i in look_up: look_up[i] += 1
		else: look_up[i] = 1

	for i in str2:
		if i not in look_up: return False
		if look_up[i] == 0: return False
		else: look_up[i] -= 1

	return True
