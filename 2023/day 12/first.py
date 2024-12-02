from typing import Tuple
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
            a, b = line.split(" ")
            lines.append(([x for x in a], [int(x) for x in b.split(",")]))
    return lines

def fit_measurement(previous, line, measurements) -> Tuple[int]:
    if len(measurements) == 0:
        final = previous + "".join(line)
        return 1 if "#" not in final else 0

    count = 0
    for i in range(len(line)):
        segment = line[i:i+measurements[0]]
        found = False

        if i != 0 and line[i - 1] == '#':
            continue

        if len(segment) != measurements[0]:
            found = False
        elif "." in segment:
            found = False
        elif all(map(lambda x: x == '#', segment)):
            found = True
        else:
            if len(line) <= i + measurements[0]:
                found = True
            elif line[i + measurements[0]] != '#':
                found = True

        if found:
            new_previous = previous + "".join(line[0:i]) + "x" * measurements[0] + "".join(line[i + measurements[0]: i + measurements[0] + 1])
            count += fit_measurement(new_previous, line[i + measurements[0] + 1:], measurements[1:])
    return count

lines = read(len(sys.argv[1:]))

count = 0
for line in lines:
    count += fit_measurement("", line[0], line[1])

print(count)
