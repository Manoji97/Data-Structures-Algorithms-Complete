'''
Reverse a Given sentence

'''

# Time complexity  is O(n)


def SentenceReversing(string):
	reverse = []
	length = len(string)

	i = 0

	while(i<length):
		if string[i] != " ":
			start = i
			while i < length and string[i] != " ":
				i += 1
			reverse.append(string[start: i])
		i +=1 

	reverse.reverse()
	return ' '.join(reverse)


print(SentenceReversing("im the best"))