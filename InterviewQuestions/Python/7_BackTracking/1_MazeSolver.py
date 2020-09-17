'''
This Function solves Maze
using Backtracking

action => up, down, left, right

1 means wall, u cannot move to 1 node

u can only traverse in node where value is 0


'''

# Using Depth First Search

'''
steps:

1) choose one in 4 movements
2) check if its valid
3) if valid recurse through it
4) mark it as valid
5) keep on doing that till you reach the end vertex
6) if you have no options and you didnt reach end vertex backtrack
7) if you visited all nodes you cannot reach end node


'''

class Maze(object):
	def __init__(self, maze_matrix):
		self.maze = maze_matrix
		self.rows = len(maze_matrix) - 1
		self.cols = len(maze_matrix[0]) - 1
		self.movements = {
			"up": (-1, 0),
			"down": (1, 0),
			"left": (0, -1),
			"right": (0, 1)
		}
		self.visited = [[0 for i in range(self.cols + 1)] for i in range(self.rows + 1)]
		self.found = False

	def isMovementValid(self, pos, movement):
		if pos[0] < 0 or pos[0] > self.rows: return False
		if pos[1] < 0 or pos[1] > self.cols: return False

		if self.maze[pos[0]][pos[1]] == 1: return False

		if pos[0] <= 0 and movement == self.movements["up"]: return False
		if pos[0] >= self.rows and movement == self.movements["down"]: return False
		if pos[1] <= 0 and movement == self.movements["left"]: return False
		if pos[1] >= self.cols and movement == self.movements["right"]: return False

		return True

	def findPath(self, start_pos, end_pos):
		self.found = False
		self.visited = [[0 for i in range(self.cols + 1)] for i in range(self.rows + 1)]
		self.solve(start_pos, end_pos)
		if self.found: return self.visited
		return False



	def solve(self, pos, end_pos):
		#print(pos)
		if (self.visited[pos[0]][pos[1]]): return False
		self.visited[pos[0]][pos[1]] = 1

		if pos == end_pos:
			self.found = True
			return True

		for action in self.movements:
			movement = self.movements[action]
			if self.isMovementValid(pos, movement) and not self.found:
				new_pos = (pos[0] + movement[0], pos[1] + movement[1])
				self.solve(new_pos, end_pos) 

		if self.found: return True

		self.visited[pos[0]][pos[1]] = 0



_maze = [[0, 0, 0, 0],
		[0, 1, 1, 0],
		[1, 0, 0, 0],
		[0, 0, 0, 0]]

maze = Maze(_maze)

print(maze.findPath((3, 0), (2,2)))
