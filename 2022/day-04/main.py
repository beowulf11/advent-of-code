def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


def is_within_range_1(r1, r2):
    if r2[0] <= r1[0] <= r2[1] and r2[0] <= r1[1] <= r2[1]:
        return True
    elif r1[0] <= r2[0] <= r1[1] and r1[0] <= r2[1] <= r1[1]:
        return True

    return False


def is_within_range_2(r1, r2):
    if r2[0] <= r1[0] <= r2[1]:
        return True
    elif r2[0] <= r1[1] <= r2[1]:
        return True
    elif r1[0] <= r2[0] <= r1[1]:
        return True
    elif r1[0] <= r2[1] <= r1[1]:
        return True

    return False


count_1 = 0
count_2 = 0
for line in load():
    p1, p2 = line.split(",")
    p1 = [int(x) for x in p1.split("-")]
    p2 = [int(x) for x in p2.split("-")]
    if is_within_range_1(p1, p2):
        count_1 += 1
    if is_within_range_2(p1, p2):
        count_2 += 1

print(f"Part 1: {count_1}")
print(f"Part 2: {count_2}")
