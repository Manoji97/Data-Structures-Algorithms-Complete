'''
You have to implement a Queue using Stacks

to do so , we need to stacks , during enqueue just append to stack1 

but during dequeue pop from stack 1 and append to stack 2 and atlasat pop

'''

class Stack(object):
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		return self.stack.pop()

	def length(self):
		return len(self.stack)


class Queue(object):
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def enqueue(self, value):
		self.stack1.push(value)
		return True

	def dequeue(self):
		if self.stack1.length() == 0: return False
		while self.stack1.length() != 0:
			self.stack2.push(self.stack1.pop())


		dequeued_value = self.stack2.pop()

		while self.stack2.length() != 0:
			self.stack1.push(self.stack2.pop())

		return dequeued_value
		

Q =  Queue()
Q.enqueue(5)
Q.enqueue(4)

Q.enqueue(3)
Q.enqueue(2)
Q.enqueue(1)
Q.enqueue(0)

print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())



