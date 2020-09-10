class Node(object):
	def __init__(self, val, priority):
		self.val = val
		self.priority = priority

	def __str__(self):
		return f'{self.val}-{self.priority}'

	def __repr__(self):
		return f'{self.val}-{self.priority}'
		

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def enqueue(self, val, priority):
		if len(self.queue) == 0:
			return self.queue.append(Node(val, priority)) != False

		self.queue.append(Node(val, priority))

		child_idx = len(self.queue) - 1

		while child_idx > 0:
			parent_idx = math.floor((child_idx-1)/2)
			child = self.queue[child_idx]
			parent = self.queue[parent_idx]

			if parent.priority <= child.priority: break

			self.queue[parent_idx], self.queue[child_idx] = self.queue[child_idx], self.queue[parent_idx]

			child_idx = parent_idx

		return True

	def dequque(self):
		if len(self.queue) == 0: return False

		new_root = self.queue.pop()
		if len(self.queue) == 0: return new_root
		max_value = self.queue[0]
		self.queue[0] = new_root
		length = len(self.queue)

		parent_idx = 0
		left_idx, right_idx = 1, 2
		new_idx = 0

		while True:
			parent = self.queue[parent_idx]

			if left_idx >= length: break
			left = self.queue[left_idx]
			if(left.priority < parent.priority):
				new_idx = left_idx

			if right_idx >= length: break
			right = self.queue[right_idx]
			if(right.priority < left.priority and right.priority < parent.priority):
				new_idx = right_idx

			if new_idx == parent_idx: break

			self.queue[new_idx], self.queue[parent_idx] = self.queue[parent_idx], self.queue[new_idx]

			parent_idx = new_idx
			left_idx = (2 * parent_idx) + 1
			right_idx = (2 * parent_idx) + 2

		return max_value

		