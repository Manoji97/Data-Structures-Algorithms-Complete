'''
for a given single linked List check if there is any cycle in between them
'''

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		return str(self.val)

	def __str__(self):
		return str(self.val)



class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def printAll(self):
		if not self.head: return False

		elements = []
		node = self.head

		while node:
			elements.append(node.val)
			node = node.next

		return elements

	def push(self, val):
		new_node = Node(val)

		if not self.head:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1

		return new_node.val

	def pop(self):
		if self.length == 0: return False
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
			self.tail = previous_node

		self.length -= 1

		return node.val


	def unshift(self, val):
		new_node = Node(val)

		if not self.head:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		self.length += 1 

		return new_node.val


	def shift(self):
		if self.length == 0: return False

		if self.length == 1:
			node = self.head
			self.head = self.tail = None
		else:
			node = self.head
			self.head = self.head.next

		self.length -= 1
		
		return node.val


	def get(self, index):
		if index >= self.length or index < 0: return False

		node = self.head
		for i in range(index):
			node = node.next

		return node

	def set(self, index, val):
		set_node = self.get(index)

		if not set_node: return False

		set_node.val = val

		return set_node


	def insert(self, index, val):
		if index < 0 or index > self.length: return False
		if index == 0: return self.unshift(val) != None
		if index == self.length: return self.push(val) != None

		prev_node = self.get(index-1)
		new_node = Node(val)
		
		new_node.next = prev_node.next
		prev_node.next = new_node
		self.length += 1

		return True


	def remove(self, index):
		if index < 0 or index > self.length-1: return False
		if index == 0: return self.shift() != False
		if index == self.length-1: return self.pop() != False

		prev_node = self.get(index-1)

		prev_node.next = prev_node.next.next
		self.length -= 1
		return True


	def reverse(self):
		if self.length == 0: return
		self.head, self.tail = self.tail, self.head

		previous = None
		current = self.tail
		
		for i in range(self.length):
			next_node = current.next
			current.next = previous

			previous = current
			current = next_node

		return

	def getNthNode(self, n):
		if not self.head: return -1
		if n > self.length: return -1

		slow = self.head
		fast = self.head

		for i in range(n):
			fast = fast.next

		while fast:
			slow = slow.next
			fast = fast.next

		return slow



			


		

	




