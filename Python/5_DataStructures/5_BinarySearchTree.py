class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)
		

class BinarySearchTree(object):
	def __init__(self):
		self.root = None
		self.totalNodes = 0

	def insert(self,val):
		if not self.root: 
			self.root = Node(val)
			self.totalNodes += 1
			return True
		else:
			def recursiveHelper(val, node = self.root):
				if val == node.val:
					return False

				if not node.left and val < node.val:
					node.left = Node(val)
					return True
				if not node.right and val > node.val:
					node.right = Node(val)
					return True

				if val < node.val:
					return recursiveHelper(val, node.left)
				else:
					return recursiveHelper(val, node.right)

			out = recursiveHelper(val)
			if out:
				self.totalNodes += 1
			return out




	def insertIteratively(self, val):
		new_node = Node(val)

		if not self.root:
			self.root = new_node
		else:
			node = self.root

			while True:
				if node.val == val: return False

				if val < node.val:
					if not node.left:
						node.left = new_node
						break
					else: node = node.left
				if val > node.val:
					if not node.right:
						node.right = new_node
						break
					else: node = node.right

		self.totalNodes += 1 
		return True



	def contains(self, val):
		if not self.root: return False

		def recursiveHelper(val, node = self.root):
			if node.val == val: return True

			if val < node.val:
				if not node.left: return False
				return recursiveHelper(val, node.left)
			else: 
				if not node.right: return False
				return recursiveHelper(val ,node.right)


		return recursiveHelper(val)

	def containsIterative(self, val):
		if not self.root: return False
		node = self.root

		while node:
			if node.val == val:return True
			if val < node.val:
				node = node.left
			else:
				node = node.right

		return False
			

		