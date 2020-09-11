class Graph(object):
	def __init__(self):
		self.adjacencyList = {}

	def removeFromList(self, lst, val):
		for idx, _val in enumerate(lst):
			if val == _val:
				lst.pop(idx)
				break
		return lst

	def addVertex(self, vertex):
		if vertex in self.adjacencyList:
			return False

		self.adjacencyList[vertex] = []
		return True

	def removeVertex(self, vertex):
		if vertex not in self.adjacencyList:
			return False

		neighbours = self.adjacencyList[vertex]

		for neighbour in neighbours:
			self.adjacencyList[neighbour] = self.removeFromList(self.adjacencyList[neighbour], vertex)

		del self.adjacencyList[vertex]

		return True


	def addEdge(self, vertex1, vertex2):
		if vertex1 not in self.adjacencyList or vertex2 not in self.adjacencyList:
			return False

		if vertex2 in self.adjacencyList[vertex1]:
			return False

		self.adjacencyList[vertex1].append(vertex2)
		self.adjacencyList[vertex2].append(vertex1)
		return True
		

	def removeEdge(self, vertex1, vertex2):
		if vertex1 not in self.adjacencyList or vertex2 not in self.adjacencyList:
			return False

		self.adjacencyList[vertex1] = self.removeFromList(self.adjacencyList[vertex1], vertex2)
		self.adjacencyList[vertex2] = self.removeFromList(self.adjacencyList[vertex2], vertex1)

		return True

	def breadthFirst(self, vertex):
		if vertex not in self.adjacencyList: return False
		queue = [vertex]
		output = []
		visited = {}

		while len(queue) != 0:
			_vertex = queue.pop(0)
			if _vertex in visited: continue

			visited[_vertex] = True
			output.append(_vertex)
			queue += self.adjacencyList[_vertex]

		return output

	def breadthFirstRecursive(self, vertex):
		def recursiveHelper(queue = [vertex], output = [], visited = {}):
			if len(queue) == 0:return output

			_vertex = queue.pop(0)

			if _vertex not in visited:
				output.append(_vertex)

				visited[_vertex] = True
				queue += self.adjacencyList[_vertex]

			return recursiveHelper(queue, output, visited)
			
		return recursiveHelper([vertex])


	def depthFirst(self, vertex):
		def DFShelper(vertex, output = [], visited = {}):
			if vertex not in visited:
				output.append(vertex)
				visited[vertex] = True

				for _vertex in self.adjacencyList[vertex]:
					DFShelper(_vertex, output, visited)
			return output
		return DFShelper(vertex)

	def depthFirst2(self, vertex):
		output = []
		visited = {}
		def DFS(vertex):
			if vertex not in visited:
				output.append(vertex)
				visited[vertex] = True

				for _vertex in self.adjacencyList[vertex]:
					DFS(_vertex)
			return output
		return DFS(vertex)


		