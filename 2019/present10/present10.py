def get_slope(y0, x0, y1, x1):
    if x0 == x1:
        return None
    if y0 == y1:
        return 0
    return (y0 - y1) / (x0 - x1)

def is_intersecting(slope, y0, x0, dy0, dx1):
    return dy1 == (slope * dx0) - (slope * x0) + y0

def get_y(slope, y0, x0, dx0):
    return slope * (dx0 - x0) + y0

def is_whole(number):
    return int(number) == float(number)

star_map = [line[:-1] for line in open("input.txt").readlines()]
stars = dict()

station = (25, 22)

for y in range(len(star_map)):
    for x in range(len(star_map[y])):
        if star_map[y][x] == "#":
            stars[(y, x)] = 0

star = base = station
neighbours = []
for neigh_star in stars:
    if star == neigh_star:
        continue

    d = get_slope(*star, *neigh_star)
    can_see = True

    if d == None:
        for y in range(min(star[0], neigh_star[0]) + 1, max(star[0], neigh_star[0])):
            if (y, star[1]) in stars:
                can_see = False
                break
    else:
        for x in range(min(star[1], neigh_star[1]) + 1, max(star[1], neigh_star[1])):
            if not can_see:
                continue
            y = get_y(d, *star, x)
            if not is_whole(y):
                continue
            y = int(y)
            if (y, x) in stars:
                can_see = False
                break

    if can_see:
        neighbours.append({'star': neigh_star, 'slope': 0 if d is None else d})


top_right = []
bottom_right = []
bottom_left = []
top_left = []

sorted_neighbours = sorted(neighbours, key=lambda x: x['slope'])

not_top_left = []
maybe_top_left = []

for neighbour in neighbours:
    neigh_star = neighbour['star']

    if neigh_star[0] < base[0] and neigh_star[1] < base[1]:
        maybe_top_left.append(neighbour)
        continue
    not_top_left.append(neighbour)

print(len(not_top_left))
print(len(maybe_top_left))
print(len(maybe_top_left) + len(not_top_left))
print(f"all = {len(sorted_neighbours)}")

print(f"base = {base}")
dead = len(not_top_left)

sorted_top_left = sorted(maybe_top_left, key=lambda x: x['slope'])

for n in sorted_top_left:
    dead += 1
    print(dead, n)
    if dead == 200:
        break

# for neighbour in sorted_neighbours:
#     neigh_star = neighbour['star']
# 
#     if neigh_star[0] > base[0] or neigh_star[1] < base[1]:
#         continue
# 
#     top_right.append(neighbour)
# 
# for neighbour in sorted_neighbours:
#     neigh_star = neighbour['star']
# 
#     if neigh_star in top_right:
#         continue
# 
#     if neigh_star[0] < base[0] or neigh_star[1] < base[1]:
#         continue
# 
#     bottom_right.append(neighbour)
# 
# for neighbour in sorted_neighbours:
#     neigh_star = neighbour['star']
# 
#     if neigh_star in top_right or neigh_star in bottom_right:
#         continue
# 
#     if neigh_star[0] < base[0] or neigh_star[1] > base[1]:
#         continue
# 
#     bottom_left.append(neighbour)
# 
# for neighbour in sorted_neighbours:
#     neigh_star = neighbour['star']
# 
#     if neigh_star in top_right or neigh_star in bottom_right or neigh_star in bottom_left:
#         continue
# 
#     if neigh_star[0] > base[0] or neigh_star[1] > base[1]:
#         continue
# 
#     top_left.append(neighbour)
# 
# print(f"top right = {len(top_right)}, bottom right = {len(bottom_right)}, bottom left = {len(bottom_left)}, top left = {len(top_left)}, sum = {len(top_right) + len(bottom_right) + len(bottom_left) + len(top_left)}")
