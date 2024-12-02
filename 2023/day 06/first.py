from functools import reduce
from math import pow
import sys
import re


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split(":")[1]
            lines.append([int(x) for x in line.split(" ") if x])
    return lines


lines = read(len(sys.argv[1:]))

print(lines)
races = [
    (time, lines[1][i]) for i, time in enumerate(lines[0])
]
print(races)

def calculate_winning_range(time, distance):
    winning_times = []
    for t in range(1, time):
        travel = t * (time - t)
        if travel > distance:
            winning_times.append(t)

    return winning_times

print(reduce(lambda acc, x: acc * x, [len(calculate_winning_range(*r)) for r in races]))
