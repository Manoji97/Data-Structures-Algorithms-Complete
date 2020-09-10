class Simple_Queue(object):
	'''
	enqueue has Time Complexity of => O(1)
	dequeue has Time Complexity of => O(n) because of shift operator
	which moves all the values one index
	
	peek takes O(1)
	'''
	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		self.queue.append(val)
		return True

	def dequeue(self):
		if len(self.queue) == 0: return False
		return self.queue.pop(0)

	def peek(self):
		if len(self.queue) == 0: return False
		return self.queue[0]



class Node(object): 
	def __init__(self, val):
		self.val = val
		self.next = None
		
		
class Queue(object):
	'''
	All the operations in this class has Time Complexity of O(1)
	'''
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def enqueue(self, val):
		new_node = Node(val)

		if not self.head:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1
		return True


	def dequeue(self):
		if self.length == 0: return False
		if self.length == 1:
			node = self.head
			self.head = self.tail = None
		else:
			node = self.head
			self.head = node

		self.length -= 1
		return node.val

	def peek(self):
		if self.length == 0: return False
		return self.head.val
		
		