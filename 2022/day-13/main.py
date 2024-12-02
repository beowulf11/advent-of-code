import json
from enum import Enum


def load():
    with open("day-13/input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Result:
	InOrder = 1
	OutOrder = 2
	Skip = 3


def compare(left, right):
	if type(left) is int and type(right) is int:
		return compare_integer(left, right)
	elif type(left) is list and type(right) is list:
		return compare_list(left, right)
	elif type(left) is int:
		return compare_list([left], right)
	else:
		return compare_list(left, [right])
		
def compare_list(left, right):
	for le, re in zip(left, right):
		cr = compare(le, re)
		if cr == Result.InOrder or cr == Result.OutOrder:
			return cr
		else:
			pass
			
	if len(left) < len(right):
		return Result.InOrder
	elif len(left) > len(right):
		return Result.OutOrder
	else:
		return Result.Skip


def compare_integer(left, right):
	if left < right:
		return Result.InOrder
	elif left > right:
		return Result.OutOrder
	else:
		return Result.Skip




#  Part 1
lines = []
tmp = []
for line in load():
	if line == "":
		lines.append(tmp)
		tmp = []
	else:
		tmp.append(json.loads(line))
lines.append(tmp)

score = 0
for i, line in enumerate(lines):
	if compare(line[0], line[1]) == Result.InOrder:
		score += i + 1
		
print(score)


#  Part 2
lines = [[[2]], [[6]]]
tmp = []
for line in load():
	if line == "":
		pass
	else:
		lines.append(json.loads(line))
lines.append(tmp)

new_order = [0]

def insert_correctly_right(indexes, lines, current, new_index):
	current_index = 0
	while True:
		if compare(lines[indexes[current_index]], current) == Result.InOrder:
			current_index += 1
			if current_index == len(indexes):
				indexes.append(new_index)
				return
		else:
			break
				
	indexes.insert(current_index, new_index)
	
def insert_correctly_left(indexes, lines, current, new_index):
	current_index = -1
	while True:
		if compare(current, lines[indexes[current_index]]) == Result.InOrder:
			current_index -= 1
			if abs(current_index) > len(indexes):
				indexes.insert(0, new_index)
				return
		else:
			break
				
	indexes.insert(current_index + 1, new_index)

#  Left
left = lines[0]
left_indexes = [0]
skip = set()
rotate = True
while rotate:
	rotate = False
	for index, line in enumerate(lines):
		if index == 0 or index in skip:
			continue
		if compare(left, line) == Result.OutOrder:
			skip.add(index)
		if compare(left, line) == Result.InOrder:
			rotate = True
			skip.add(index)
			insert_correctly_right(left_indexes, lines, line, index)
			
right = lines[0]
right_indexes = [0]
skip = set()
skip.update(left_indexes)
rotate = True
while rotate:
	rotate = False
	for index, line in enumerate(lines):
		if index == 0 or index in skip:
			continue
		if compare(line, right) == Result.OutOrder:
			skip.add(index)
		if compare(line, right) == Result.InOrder:
			rotate = True
			skip.add(index)
			insert_correctly_left(right_indexes, lines, line, index)

right_indexes.pop()
new_order = right_indexes + left_indexes
score = []
for index, no in enumerate(new_order):
	if no == 0 or no == 1:
		score.append(index)
print(score[0] * score[1])