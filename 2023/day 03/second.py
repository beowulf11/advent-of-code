import sys
import re


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines

def is_number(c) -> bool:
    try:
        int(c)
        return True
    except ValueError:
        return False


def add_matches(row, start, end):
    r_start = max(start - 1, 0)
    r_end = min(line_width, end + 1)

    for i in range(r_start, r_end):
        if (row - 1, i) in symbols:
            match = matches.get((row - 1, i), list()) + [(row, start, end)]
            matches[(row - 1, i)] = match
        if (row + 1, i) in symbols:
            match = matches.get((row + 1, i), list()) + [(row, start, end)]
            matches[(row + 1, i)] = match

    if (row, r_start) in symbols:
        match = matches.get((row, r_start), list()) + [(row, start, end)]
        matches[(row, r_start)] = match
    if (row, end) in symbols:
        match = matches.get((row, end), list()) + [(row, start, end)]
        matches[(row, end)] = match


lines = read(len(sys.argv[1:]))
line_width = len(lines[0])
symbols = set()  # (row, column) set of symbols
result = 0
matches = {}

for row_index, line in enumerate(lines):
    for column_index, c in enumerate(line):
        if c == '.' or is_number(c):
            continue
        symbols.add((row_index, column_index))

for row_index, line in enumerate(lines):
    indexes = re.finditer(r'\d+', line)
    for match in indexes:
        add_matches(row_index, *match.span())

for match in matches.values():
    if len(match) != 2:
        continue
    match1 = int(lines[match[0][0]][match[0][1]:match[0][2]])
    match2 = int(lines[match[1][0]][match[1][1]:match[1][2]])
    result += match1 * match2

print(result)
