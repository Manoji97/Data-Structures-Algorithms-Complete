'''
Anagram is Two Strings with extact Letters


Time Complexity is O(n)
'''

def CheckAnagram(str1, str2):
	if(len(str1) != len(str2)): return False

	str1_dict = {}

	for i in str1:
		if(i in str1_dict):
			str1_dict[i] += 1
		else: str1_dict[i] = 1

	for i in str2:
		if(i in str1_dict):
			if(str1_dict[i] == 0): return False
			str1_dict[i] -= 1
		else: return False


	return True

print(CheckAnagram("lLevel", "LLevel"))