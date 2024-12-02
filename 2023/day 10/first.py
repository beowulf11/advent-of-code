from typing import Tuple
from dataclasses import dataclass
from math import pow
import sys
import re


def read(test: bool = False):
    lines = []
    with open("test2.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append([x for x in line])
    return lines


def get_neighbors(y: int, x: int):
    c = lines[y][x]
    match c:
        case "|":
            return ((y - 1, x), (y + 1, x))
        case "-":
            return ((y, x - 1), (y, x + 1))
        case "L":
            return ((y - 1, x), (y, x + 1))
        case "J":
            return ((y - 1, x), (y, x - 1))
        case "7":
            return ((y + 1, x), (y, x - 1))
        case "F":
            return ((y + 1, x), (y, x + 1))
        case ".":
            return None,
        case "S":
            return get_start_neighbors(y, x)


def get_start_neighbors(y, x):
    possible_neighbors = []
    position = (y, x)
    for ix in range(x - 1, x + 2):
        if position in get_neighbors(y-1, ix):
            possible_neighbors.append((y-1, ix))

    if position in get_neighbors(y, x - 1):
        possible_neighbors.append((y, x - 1))

    if position in get_neighbors(y, x + 1):
        possible_neighbors.append((y, x + 1))

    for ix in range(x - 1, x + 2):
        if position in get_neighbors(y+1, ix):
            possible_neighbors.append((y+1, ix))

    return possible_neighbors

def get_next(previous, current):
    possible = get_neighbors(*current)
    if possible[0] == previous:
        return (current, possible[1])
    if possible[1] == previous:
        return (current, possible[0])

    print(possible)
lines = read(len(sys.argv[1:]))
s_position = None
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            s_position = (y, x)
            break

previous, current = s_position, get_start_neighbors(*s_position)[0]
length = 0
while True:
    previous, current = get_next(previous, current)
    length += 1
    if current == s_position:
        break

print((length + 1) / 2)
