
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
            line = filter(lambda x: x, line.split(":")[1].split(" "))
            lines.append(int("".join(line)))
    return lines


race = read(len(sys.argv[1:]))

def calculate_winning_range(time, distance):
    first_time = None
    last_time = None

    for t in range(1, time):
        travel = t * (time - t)
        if travel > distance:
            first_time = t
            break

    for t in range(time, 1, -1):
        travel = t * (time - t)
        if travel > distance:
            last_time = t
            break

    return last_time - first_time + 1

print(calculate_winning_range(*race))
