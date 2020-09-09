'''
Given a string if all the chars are unique 
	return True
else 
	return False
'''

# Time complexity  is O(n)

def IsAllCharsUnique(string):
	string_dict = {}

	for i in string:
		if i in string_dict: return False
		else: string_dict[i] = 1 

	return True

print(IsAllCharsUnique("aebcde"))