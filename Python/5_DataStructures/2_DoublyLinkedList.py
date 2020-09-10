class Node(object):
	def __init__(self, val):
		self.val = val
		self.previous = None
		self.next = None
		
class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def printAll(self):
		elements = []
		node = self.head

		while(node):
			elements.append(node.val)
			node = node.next

		return elements
		
	def push(self, val):
		new_node = Node(val)

		if self.length == 0:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.previous = self.tail
			self.tail = new_node

		self.length += 1
		return True

	def pop(self):
		if self.length == 0: return False
		if self.length == 1: 
			self.head = self.tail = None
		else:
			node = self.tail
			self.tail = node.previous
			self.tail.next = None
			node.previous = None

		self.length -= 1
		return node.val

	def unshift(self, val):
		new_node = Node(val)
		if self.length == 0: 
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node

		self.length += 1
		return True

	def shift(self):
		if self.length == 0: return False
		if self.length == 1:
			node = self.head
			self.head = self.tail = None
		else:
			node = self.head
			self.head = node.next
			self.head.previous = None
			node.next = None

		self.length -= 1
		return node

	def get(self, index):
		if index < 0 or index >= self.length: return False
		if index < int(self.length/2):
			node = self.head
			for i in range(index):
				node = node.next
		else:
			node = self.tail
			for i in range(self.length-index - 1):
				node = node.previous

		return node

	def set(self, index, val):
		set_node = self.get(index)
		if not set_node: return False

		set_node.val = val

		return True

	def insert(self, index, val):
		if index < 0 or index > self.length: return False
		if index == 0: return self.unshift(val) != False
		if index == self.length: return self.push(val) != False

		new_node = Node(val)
		previous_node = self.get(index-1)
 
		new_node.next = previous_node.next
		previous_node.next.previous = new_node
		new_node.previous = previous_node
		previous_node.next = new_node

		self.length += 1
		return True

	def remove(self, index):
		if index < 0 or index >= self.length: return False
		if index == 0: return self.shift() != False
		if index == self.length-1: return self.pop() != False

		index_node = self.get(index)

		previous_node = index_node.previous
		next_node = index_node.next
		previous_node.next = next_node
		next_node.previous = previous_node

		self.length -= 1
		return True

	def reverse(self):
		if self.length == 0: return
		self.head, self.tail = self.tail, self.head

		node = self.tail
		for i in range(self.length):
			_next = node.next
			node.next = node.previous
			node.previous = _next

			node = _next

		return True