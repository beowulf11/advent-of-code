import sys


def load():
    with open("day-14/input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())
		
class Maze:
	def __init__(self):
		self.rocks = set()
		self.sand = set()
		self.min_x = 999999999
		self.max_x = 0
		
		self.min_y = 999999999
		self.max_y = 0
		
	def add_rock(self, from_path, to_path):
		if from_path[0] != to_path[0]:
			f = min(from_path[0], to_path[0])
			t = max(from_path[0], to_path[0])
			for i in range(f, t + 1):
				self.rocks.add((i, from_path[1]))
		else:
			f = min(from_path[1], to_path[1])
			t = max(from_path[1], to_path[1])
			for i in range(f, t + 1):
				self.rocks.add((from_path[0], i))
				
		self.min_x = min(self.min_x, from_path[0], to_path[0])
		self.min_y = min(self.min_y, from_path[1], to_path[1])
		
		self.max_x = max(self.max_x, from_path[0], to_path[0])
		self.max_y = max(self.max_y, from_path[1], to_path[1])
		
	def is_free_1(self, pos):
		if pos in self.rocks or pos in self.sand:
			return False
		return True
		
	def is_free_2(self, pos):
		if pos in self.rocks or pos in self.sand:
			return False
		elif pos[1] >= self.max_y + 2:
			return False
		return True
		
	def start_sand_1(self):
		pour_sand = True
		count = 0
		while pour_sand:
			pos = (500, 0)
			while True:
				new_pos = None
				if self.is_free_1((pos[0], pos[1]+1)):
					new_pos = (pos[0], pos[1]+1)
				elif self.is_free_1((pos[0]-1, pos[1]+1)):
					new_pos = (pos[0]-1, pos[1]+1)
				elif self.is_free_1((pos[0]+1, pos[1]+1)):
					new_pos = (pos[0]+1, pos[1]+1)
				else:
					self.sand.add(pos)
					break

				if new_pos[1] > self.max_x:
					pour_sand = False
					break
				pos = new_pos
		
	def start_sand_2(self):
		pour_sand = True
		count = 0
		while pour_sand:
			pos = (500, 0)
			while True:
				new_pos = None
				if self.is_free_2((pos[0], pos[1]+1)):
					new_pos = (pos[0], pos[1]+1)
				elif self.is_free_2((pos[0]-1, pos[1]+1)):
					new_pos = (pos[0]-1, pos[1]+1)
				elif self.is_free_2((pos[0]+1, pos[1]+1)):
					new_pos = (pos[0]+1, pos[1]+1)
				else:
					self.sand.add(pos)
					if pos == (500, 0):
						pour_sand = False
						break
					break

				pos = new_pos
		
	def print(self, current=None):
		for y in range(self.min_y-15, self.max_y+3):
			for x in range(self.min_x-2, self.max_x+2):
				if (x, y) == current:
					print("~", end="")
				if (x, y) in self.rocks:
					print("#", end="")
				elif (x, y) in self.sand:
					print("+", end="")
				else:
					print(".", end="")
			print()


paths = []
for line in load():
	path = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), line.split(" -> ")))
	paths.append(path)
maze = Maze()
for path in paths:
	for index in range(len(path) - 1):
		maze.add_rock(path[index], path[index+1])
	
	
#  Part 1
maze.start_sand_1()
# maze.print()
print(f"Sand count = {len(maze.sand)}\n")


#  Part 2
maze.sand = set()
maze.start_sand_2()
# maze.print()
print(f"Sand count = {len(maze.sand)}")
