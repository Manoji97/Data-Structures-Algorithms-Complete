import math

class BinaryHeap(object):
	def __init__(self):
		self.heap = []

	def insert(self, val):
		if len(self.heap) == 0:
			return self.heap.append(val)

		self.heap.append(val)

		child_idx = len(self.heap) - 1

		while child_idx > 0:
			parent_idx = math.floor((child_idx-1)/2)
			child = self.heap[child_idx]
			parent = self.heap[parent_idx]

			if parent >= child: break

			self.heap[parent_idx], self.heap[child_idx] = self.heap[child_idx], self.heap[parent_idx]

			child_idx = parent_idx

		return True


	def extractMax(self):
		if len(self.heap) == 0: return False
		if len(self.heap) == 1:
			return self.heap.pop()

		new_root = self.heap.pop()
		max_value = self.heap[0]
		self.heap[0] = new_root
		length = len(self.heap)

		parent_idx = 0
		left_idx, right_idx = 1, 2
		new_idx = 0

		while True:
			parent = self.heap[parent_idx]

			if left_idx >= length: break
			left = self.heap[left_idx]
			if(left > parent):
				new_idx = left_idx

			if right_idx >= length: break
			right = self.heap[right_idx]
			if(right > left and right > parent):
				new_idx = right_idx

			if new_idx == parent_idx: break

			self.heap[new_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[new_idx]

			parent_idx = new_idx
			left_idx = (2 * parent_idx) + 1
			right_idx = (2 * parent_idx) + 2

		return max_value