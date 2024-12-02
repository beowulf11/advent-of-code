from dataclasses import dataclass
from math import pow
import sys
import re


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append([x for x in line])
    return lines

lines = read(len(sys.argv[1:]))


galaxies = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            galaxies.append((y, x))

empty_rows = [i for i in range(len(lines)) if all(x == '.' for x in lines[i])]
empty_columns = [i for i in range(len(lines[0])) if all(lines[y][i] == '.' for y in range(len(lines)))]
multiplier = 1000000
multiplier -= 1
for i, row in enumerate(empty_rows):
    for g in range(len(galaxies)):
        if galaxies[g][0] - (i * multiplier) > row:
            galaxies[g] = galaxies[g][0] + multiplier, galaxies[g][1]

for i, column in enumerate(empty_columns):
    for g in range(len(galaxies)):
        if galaxies[g][1] - (i * multiplier) > column:
            galaxies[g] = galaxies[g][0], galaxies[g][1] + multiplier

# width = max([x[1] for x in galaxies])
# height = max([x[0] for x in galaxies])
# for y in range(height + 1):
#     for x in range(width + 1):
#         if (y, x) in galaxies:
#             print('#', end="")
#         else:
#             print('.', end="")
#     print()

distance_sum = 0
for i in range(len(galaxies[:-1])):
    for j in range(i + 1, len(galaxies)):
        distance_sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(distance_sum)
