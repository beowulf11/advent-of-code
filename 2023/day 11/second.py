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
            lines.append([int(x) for x in line.split(" ")])
    return lines

class Reading:
    def __init__(self, readings):
        self.readings = readings

        rows = [readings]
        while True:
            row = rows[-1]
            next_row = [row[i+1] - row[i] for i in range(0, len(row) - 1)]
            rows.append(next_row)
            if sum(next_row) == 0:
                break
        self.rows = rows

    def calculate_next(self):
        previous_value = 0
        for i in range(len(self.rows) - 2, -1, -1):
            previous_value = self.rows[i][0] - previous_value

        return previous_value


lines = read(len(sys.argv[1:]))
readings = [Reading(line) for line in lines]

print(sum([r.calculate_next() for r in readings]))
