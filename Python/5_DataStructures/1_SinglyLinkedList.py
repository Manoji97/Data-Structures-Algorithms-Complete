'''
for a given single linked List check if there is any cycle in between them
'''

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None



class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def printAll(self):
		if !self.head: return False

		elements = []
		node = self.head

		while node:
			elements.append(node.val)
			node = node.next

		return elements

	def push(self, val):
		new_node = Node(val)

		if !self.head:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1

		return new_node.val

	def pop(self):
		if self.length == 1:
			node = self.head
			self.head = self.tail = None
		else:
			node = self.head
			previous_node = node

			while node != self.tail:
				previous_node = node
				node = node.next

			previous_node.next = None
			this.tail = previous_node

		this.length -= 1

		return node.val


	def unshift(self, val):
		new_node = Node(val)

		if !self.head:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		self.length += 1 

		return new_node.val


	def shift(self):
		if self.length == 1:
			node = self.head
			self.head = self.tail = None
		else:
			node = self.head
			self.head = self.head.next
		
		return node.val


	def get(self, index):
		if index > self.length or index < 0: return False

		node = self.head
		for i in range(index):
			node = node.next

		return node

	def set(self, index, val):
		set_node = self.get(index)

		if !set_node: return False

		set_node.val = val

		return set_node


	def insert(self, index, val):
		if index < 0 or index > self.length: return False
		if index == 0: self.unshift(val)
		if index == self.length: self.push(val)

		prev_node = self.get(index-1)
		new_node = Node(val)
		
		new_node.next = prev_node.next
		prev_node.next = new_node
		self.length += 1

		return True


	def remove(self, index):
		if index < 0 or index > self.length-1: return False
		if index == 0: self.shift()
		if index == self.length-1: self.pop()

		prev_node = self.get(index-1)

		prev_node.next = prev_node.next.next
		self.length -= 1
		return True


	def reverse(self):
		pass

	




