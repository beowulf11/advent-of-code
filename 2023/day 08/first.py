from dataclasses import dataclass
from math import pow
import sys
import re


def read(test: bool = False):
    paths = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        raw_lines = f.readlines()
        direction = raw_lines[0][:-1]
        for line in raw_lines[2:]:
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split(" = ")
            paths.append(Path(line[0], *line[1][1:-1].split(", ")))
    return direction, paths

class Path:
    def __init__(self, current, left, right):
        self.current = current
        self.left = left
        self.right = right
        self.is_finish = self.current == "ZZZ"

    def next(self, direction):
        if direction == "L":
            return self.left
        elif direction == "R":
            return self.right

        raise RuntimeError("fml")

    def __hash__(self):
        return hash(self.current)

    def __repr__(self):
        return f"{self.current} = ({self.left.current}, {self.right.current})"


direction, paths = read(len(sys.argv[1:]))
path_direction = {hash(p): p for p in paths}
for p in path_direction.values():
    p.left = path_direction[hash(p.left)]
    p.right = path_direction[hash(p.right)]
    print(p)


step_count = 0
current = path_direction[hash("AAA")]
while True:
    dir = direction[step_count % len(direction)]
    step_count += 1

    current = current.next(dir)
    if current.is_finish:
        break

print(step_count)
