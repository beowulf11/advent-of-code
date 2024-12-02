from dataclasses import dataclass
from math import pow, gcd, lcm
import sys
import re


def read(test: bool = False):
    paths = []
    with open("test2.txt" if test else "input.txt", "r") as f:
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
        self.is_finish = self.current[-1] == "Z"

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


nodes = [p for p in paths if p.current[-1] == 'A']
cycles = [0 for _ in nodes]

for i, node in enumerate(nodes):
    step_count = 0
    visited = set()
    node_cycles = []
    while True:
        dir = direction[step_count % len(direction)]
        node = node.next(dir)
        if (hash(node), step_count % len(direction)) in visited:
            cycles[i] = gcd(*node_cycles)
            break
        visited.add((hash(node), step_count % len(direction)))
        step_count += 1
        if node.is_finish:
            node_cycles.append(step_count)

print(" -- ")

print(lcm(*cycles))


# step_count = 0
# while True:
#     dir = direction[step_count % len(direction)]
#     for i, n in enumerate(nodes):
#         nodes[i] = n.next(dir)

#     step_count += 1
#     if all(map(lambda p: p.is_finish, nodes)):
#         break

# print(step_count)
