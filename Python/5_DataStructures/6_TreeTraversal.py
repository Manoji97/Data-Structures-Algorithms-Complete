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


	def insert(self, val):
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
		node = self.root

		while node:
			if node.val == val:return True
			if val < node.val:
				node = node.left
			else:
				node = node.right

		return False
		

	def breadthFirst(self):
		if not self.root: return False
		queue = [self.root]
		output = []

		while len(queue) != 0:
			node = queue.pop(0)
			output.append(node.val)

			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)

		return output

	def breadthFirstRecursive(self):
		if not self.root: return False
		queue = [self.root]

		def BFS(queue, output= []):
			if len(queue) == 0: return output

			node = queue.pop(0)

			output.append(node.val)

			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)

			return BFS(queue, output)

		return BFS(queue)


	def depthFirstPreOrder(self):
		def DFSpreOrder(node = self.root, output=[]):
			if not node: return output

			output.append(node.val)

			DFSpreOrder(node.left, output)
			DFSpreOrder(node.right, output)

			return output

		return DFSpreOrder()

	def depthFirstPostOrder(self):
		output = []
		def DFSPostOrder(node =self.root):
			if not node: return

			DFSPostOrder(node.left)
			DFSPostOrder(node.right)
			output.append(node.val)

			return

		DFSPostOrder()

		return output

	def depthFirstInOrder(self):
		output = []
		def DFSInorder(node = self.root):
			if node.left:  DFSInorder(node.left)
			output.append(node.val)
			if node.right:  DFSInorder(node.right)
			return

		DFSInorder()

		return output





		