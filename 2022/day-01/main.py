scores = [0]
with open("input-1.txt") as f:
    index = 0
    for line in map(lambda x: x[:-1], f.readlines()):
        if line == "":
            index += 1
            scores.append(0)
        else:
            scores[index] += int(line)

print(max(scores))
print(sum(sorted(scores)[-3:]))
