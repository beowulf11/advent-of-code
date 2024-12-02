def read():
    lines = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines

lines = read()
result = []

for line in lines:
    first = None
    last = None
    for c in line:
        try:
            n = int(c)
            if first is None:
                first = n
            last = n
        except ValueError:
            continue
    result.append(first * 10 + last)

print(sum(result))
