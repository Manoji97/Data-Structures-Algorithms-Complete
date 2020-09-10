class Stack(object):
	'''
	All the operations in this class has Time Complexity of O(1)
	'''
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)
		return True

	def pop(self):
		if len(self.stack) == 0: return False
		return self.stack.pop()

	def peek(self):
		if len(self.stack) == 0: return False
		return self.stack[-1]
		