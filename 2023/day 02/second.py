from functools import reduce


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines

lines = read(False)

result = 0
for index, line in enumerate(lines):
    line = line.split(": ")[1]
    current = {}
    for round in line.split("; "):
        for pick in round.split(", "):
            count, pick = pick.split(" ")
            current[pick] = max(current.get(pick, 0), int(count))

    result += reduce(lambda x, y: x * y, current.values(), 1)

print(result)