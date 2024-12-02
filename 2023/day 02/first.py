def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines

lines = read(False)
targets = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

result = 0
for index, line in enumerate(lines):
    line = line.split(": ")[1]
    current = {}
    for round in line.split("; "):
        for pick in round.split(", "):
            count, pick = pick.split(" ")
            current[pick] = max(current.get(pick, 0), int(count))

    passed = True
    for pick in targets.keys():
        if current[pick] > targets[pick]:
            passed = False

    if passed:
        result += index + 1

print(result)
