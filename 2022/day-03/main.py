def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


def get_value(ascii_value):
    if ascii_value < 91:
        return ascii_value - 38
    else:
        return ascii_value - 96


lines = list(load())

# Part1
rucksacks = map(lambda l: (set(l[:len(l) // 2]), set(l[len(l) // 2:])), lines)
value = sum(map(lambda r: get_value(ord(r[0].intersection(r[1]).pop())), rucksacks))
print(f"Part 1: {value}")

# Part 2
rucksacks = list(map(lambda l: set(l), lines))
value = sum(map(lambda i: get_value(ord(rucksacks[i].intersection(rucksacks[i + 1]).intersection(rucksacks[i + 2]).pop())), range(0, len(rucksacks), 3)))
print(f"Part 2: {value}")
