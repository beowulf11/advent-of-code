f = open("text.txt")
coords = []
line = f.readline()
while line:
    c1, c2 = line[:-1].split(", ")
    coords.append((int(c2), int(c1)))
    line = f.readline()


f.close()

def dist(a, b):
    v_d = None
    if a[0] > b[0]:
        v_d = len(range(b[0], a[0]))
    else:
        v_d = len(range(a[0], b[0]))

    h_d = None
    if a[1] > b[1]:
        h_d = len(range(b[1], a[1]))
    else:
        h_d = len(range(a[1], b[1]))

    return v_d + h_d

def get_min_distance_from_arr(cell, arr):
    min_distance = None
    prvok = None
    debug = (3, 5)
    distances = []
    for x in arr:
        distance = dist(x, cell)
        distances.append((distance, x))

    min_dist = min(distances, key=lambda x: x[0])
    if [x[0] for x in distances].count(min_dist) > 1:
        return None
    return min_dist[1]

def prety(x):
    if x == ".":
        return "."
    if x == (1, 1):
        return "A"
    if x == (6, 1):
        return "B"
    if x == (3, 8):
        return "C"
    if x == (4, 3):
        return "D"
    if x == (5, 5):
        return "E"
    if x == (9, 8):
        return "F"
    return x

def categorize_points():
    for point in coords:
        if check_infinity(point):
            infinite.add(point)
        else:
            finite.add(point)

def spiral(cell):
    '''Returns None after each level'''

    def sub_spiral(cell, level):
        level = level * 2 + 1 
        x, y = cell[0] - (level - 1)//2, cell[1] - (level - 1)//2
        for xx in range(x, x + level):
            yield (xx, y)
            yield (xx, y + level - 1)

        for yy in range(y - 1, y + level - 1):
            yield (x, yy)
            yield (x + level - 1, yy)

    level = 1
    while True:
        yield from sub_spiral(cell, level)
        level += 1
        yield None

infinite = set()

min_x = min(coords, key=lambda x: x[0])[0]
max_x = max(coords, key=lambda x: x[0])[0] + 1
min_y = min(coords, key=lambda x: x[1])[1]
max_y = max(coords, key=lambda x: x[1])[1] + 1

shift = min_x

pole = [[0 for x in range(max_x - min_x)] for x in range(max_y - min_y)]

for i in range(len(pole)):
    for j in range(len(pole[i])):
        if (i+shift, j+shift) in coords:
            continue
        new_coords = [x for x in coords if x != (i+shift, j+shift)]
        distance = get_min_distance_from_arr((i+shift, j+shift), new_coords)
        #print(i, j)
        if distance is not None:
            pole[i][j] = distance
        else:
            pole[i][j] = "."


counts = dict()
for x in pole:
    for y in x:
        if y == ".":
            continue
        counts[y] = counts.get(y, 0) + 1

for x in range(len(pole)):
    if x == 0 or x == len(pole) - 1:
        for y in range(len(pole[x])):
            infinite.add(pole[x][y])
            infinite.add(pole[x][len(pole[x]) - 1])
    print(pole[x][0])
    print(pole[x][len(pole[x]) - 1])
    infinite.add(pole[x][0])
    infinite.add(pole[x][len(pole[x]) - 1])

print(infinite)

max_p = None
max_d = 0
for x in counts:
    if x not in infinite:
        if counts[x] > max_d:
            max_p = x
            max_d = counts[x]

print(max_d, max_p)
