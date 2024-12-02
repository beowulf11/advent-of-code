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

def is_valid_number(row, start, end) -> bool:
    r_start = max(start - 1, 0)
    r_end = min(line_width, end + 1)

    for i in range(r_start, r_end):
        if (row - 1, i) in symbols:
            return True
        if (row + 1, i) in symbols:
            return True
    if (row, r_start) in symbols or (row, end) in symbols:
        return True

    return False

lines = read(len(sys.argv[1:]))
line_width = len(lines[0])
symbols = set()  # (row, column) set of symbols
result = 0

for row_index, line in enumerate(lines):
    for column_index, c in enumerate(line):
        if c == '.' or is_number(c):
            continue
        symbols.add((row_index, column_index))

for row_index, line in enumerate(lines):
    indexes = re.finditer(r'\d+', line)
    for match in indexes:
        if is_valid_number(row_index, *match.span()):
            result += int(match.group())

print(result)
