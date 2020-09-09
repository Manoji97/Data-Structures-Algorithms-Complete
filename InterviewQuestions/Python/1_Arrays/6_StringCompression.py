'''

given a String compress it like this 

AAaa => A2a2
AAb  => A2b1
AAABBCCC   => A3B2C3
'''

# Time complexity  is O(n)


def StringCompression(string):

	compressed = ''
	length = len(string)

	i = 1
	count = 1
	while (i < length):
		if string[i] == string[i-1]:
			count += 1
		else: 
			compressed += string[i-1] + str(count)
			count = 1

		i += 1

	compressed += string[i-1] + str(count)
	return compressed


print(StringCompression("AAABBCCC"))