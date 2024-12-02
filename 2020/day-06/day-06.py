def load_input():
    with open("input.txt") as file:
        return list(map(lambda line: line[:-1], file.readlines()))


puzzle_input = load_input()

print(" -- Part 1 --")

group_counts = []
group = set()
for line in puzzle_input:
    if line == "":
        group_counts.append(len(group))
        group = set()
    else:
        group.update(map(lambda x: x, line))

print(sum(group_counts))


print(" -- Part 2 --")

group_counts = []
group = set()
new_group = True
for line in puzzle_input:
    if line == "":
        group_counts.append(len(group))
        group = set()
        new_group = True
    else:
        if new_group:
            new_group = False
            group = set(map(lambda x: x, line))
        else:
            group = group & set(map(lambda x: x, line))

print(sum(group_counts))
