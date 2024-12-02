from typing import Tuple, List
from dataclasses import dataclass
from math import pow
import sys
import re


def read(test) -> List[List[str]]:
    lines = []
    if test:
        filename = f"test{test}.txt"
    else:
        filename = "input.txt"

    with open(filename, "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append([x for x in line])
    return lines

class Field:
    def __init__(self, points: List[List[str]]):
        self.points = points
        self.s_position: Tuple[int, int]

        for y, x in self.traverse():
            if points[y][x] == "S":
                self.s_position = (y, x)
                break

    def traverse(self):
        for y in range(len(self.points)):
            for x in range(len(self.points[y])):
                yield (y, x)

    def get(self, y, x):
        return self.points[y][x]

    def get_interpreted(self, y, x):
        c = self.get(y, x)
        if c == "S":
            start_neighbors = tuple(self.get_start_neighbors(*self.s_position))
            if start_neighbors == ((y - 1, x), (y, x - 1)):
                c = "J"
            elif start_neighbors == ((y - 1, x), (y, x + 1)):
                c = "L"
            elif start_neighbors == ((y - 1, x), (y + 1, x)):
                c = "|"
            elif start_neighbors == ((y, x - 1), (y, x + 1)):
                c = "-"
            elif start_neighbors == ((y, x - 1), (y + 1, x)):
                c = "7"
            elif start_neighbors == ((y, x + 1), (y + 1, x)):
                c = "F"
        return c

    def get_borders(self, y, x):
        match self.get_interpreted(y, x):
            case "|":
                return (
                    set([(y, x - 1)]),
                    set([(y, x + 1)]),
                )
            case "-":
                return (
                    set([(y - 1, x)]),
                    set([(y + 1, x)]),
                )
            case "L":
                return (
                    set([(y + 1, x), (y + 1, x - 1), (y, x - 1)]),
                    set([(y - 1, x + 1)]),
                )
            case "J":
                return (
                    set([(y - 1, x - 1)]),
                    set([(y, x + 1), (y + 1, x + 1), (y + 1, x)]),
                )
            case "7":
                return (
                    set([(y + 1, x - 1)]),
                    set([(y - 1, x), (y - 1, x + 1), (y, x + 1)]),
                )
            case "F":
                return (
                    set([(y, x - 1), (y - 1, x - 1), (y - 1, x)]),
                    set([(y + 1, x + 1)]),
                )

    def get_neighbors(self, y: int, x: int):
        neighbors = set()
        if y - 1 >= 0:
            neighbors.add((y - 1, x))
        if x - 1 >= 0:
            neighbors.add((y, x - 1))

        if y + 1 < len(self.points):
            neighbors.add((y + 1, x))
        if x + 1 < len(self.points[0]):
            neighbors.add((y, x + 1))
        return neighbors

    def get_path_neighbors(self, y: int, x: int):
        c = self.get(y, x)
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


    def get_start_neighbors(self, y, x):
        possible_neighbors = []
        position = (y, x)
        for ix in range(x - 1, x + 2):
            if position in self.get_path_neighbors(y-1, ix):
                possible_neighbors.append((y-1, ix))

        if position in self.get_path_neighbors(y, x - 1):
            possible_neighbors.append((y, x - 1))

        if position in self.get_path_neighbors(y, x + 1):
            possible_neighbors.append((y, x + 1))

        for ix in range(x - 1, x + 2):
            if position in self.get_path_neighbors(y+1, ix):
                possible_neighbors.append((y+1, ix))

        return possible_neighbors

class Circle:
    def __init__(self, field):
        self.field = field
        self.points, self.path = self.find_circle()
        self.inner, self.outer = self.find_border()

    def find_circle(self):
        previous, current = field.s_position, field.get_start_neighbors(*field.s_position)[0]
        points = set()
        path = [previous]
        points.add(previous)
        while True:
            points.add(current)
            path.append(current)
            previous, current = self.get_next(previous, current)
            if current == field.s_position:
                break
        return points, path

    def find_border(self):
        a, b = set(), set()
        previous = self.field.get_interpreted(*self.path[0])
        pa, pb = self.field.get_borders(*self.path[0])
        a |= pa
        b |= pb
        for point in self.path[1:]:
            current = self.field.get_interpreted(*point)
            ca, cb = self.field.get_borders(*point)
            if current == '|' and previous == '|':
                if list(pa)[0][1] != list(ca)[0][1]:
                    ca, cb = cb, ca
            elif current == '-' and previous == '-':
                if list(pa)[0][0] != list(ca)[0][0]:
                    ca, cb = cb, ca
            else:
                if len((pa | pb) & (ca | cb)) == 0:
                    if len(pa) != len(ca):
                        ca, cb = cb, ca
                elif len((pa | pb) & (ca | cb)) == 2:
                    if len(pa) == len(ca):
                        ca, cb = cb, ca
                elif len(pa & ca) == 0 and len(pb & cb) == 0:
                    ca, cb = cb, ca

            a |= ca
            b |= cb
            previous, pa, pb = current, ca, cb

        a -= self.points
        b -= self.points
        if len(a) < len(b):
            return a, b
        else:
            return b, a

    def get_next(self, previous, current):
        possible = self.field.get_path_neighbors(*current)
        if possible[0] == previous:
            return (current, possible[1])
        if possible[1] == previous:
            return (current, possible[0])

    def __contains__(self, other):
        return other in self.points


class Fill:
    def __init__(self, starting, circle, field):
        self.circle = circle
        self.field = field
        self.points = self.flood(starting)

    def __contains__(self, other):
        return other in self.points

    def flood(self, starting):
        queue = set()
        queue.add(starting)
        visited = set()
        while queue:
            el = queue.pop()
            visited.add(el)
            for neighbor in field.get_neighbors(*el):
                if neighbor in circle:
                    continue
                if neighbor in visited:
                    continue
                if neighbor in queue:
                    continue
                queue.add(neighbor)

        return visited

    def display(self, c):
        lines = []
        line = []
        previous_line = None
        for pos in self.field.traverse():
            if previous_line is not None and previous_line != pos[0]:
                lines.append("".join(line))
                line = []
            previous_line = pos[0]
            line.append((c if pos in self else '.'))
        lines.append("".join(line))
        return "\n".join(lines)


field = Field(read(int(sys.argv[1]) if sys.argv[1:] else None))
circle = Circle(field)
fills = []
visited_points = set()
for p in field.traverse():
    if p not in circle and p not in visited_points:
        fills.append(Fill(p, circle, field))
        visited_points |= fills[-1].points


print(sum([len(f.points) for f in fills if len(f.points & circle.inner)]))
# for f in fills:
#     if len(f.points & circle.inner):
#         print("Inner")
#         print(f.points)
#     else:
#         print("Outer")
#         print(f.points)

for y in range(len(field.points)):
    for x in range(len(field.points[y])):
        p = (y, x)
        if p in circle.points:
            c = "."
        elif p in circle.inner:
            c = 'i'
        elif p in circle.outer:
            c = 'o'
        else:
            c = 'x'
        print(c, end='')
    print()
