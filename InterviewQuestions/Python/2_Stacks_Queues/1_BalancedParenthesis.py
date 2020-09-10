'''
Check if the Input String consists of Balanced Parenthesis
the 3 parenthesis are {}, [], ()
'''

def CheckParenthesisBalanced(string):
	# if length is odd then its not balanced
	if len(string) % 2 != 0: return False

	stack = []

	open_parenthesis = '{[('
	matches = [('{','}'), ('[', ']'), ('(', ')')]

	for i in string:
		if i in open_parenthesis:
			stack.append(i)
		else:
			if len(stack) == 0: return False
			prev = stack.pop()
			if (prev, i) not in matches:
				return False

	return len(stack) == 0

print(CheckParenthesisBalanced('[[[]]'))
