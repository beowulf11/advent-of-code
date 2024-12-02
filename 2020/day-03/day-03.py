from functools import reduce

def load_input():
    with open("input.txt") as file:
        return list(map(lambda line: line[:-1], file.readlines()))

def next_coords_and_character(vertical_coord, horizontal_coord):
    true_vertical_coord = vertical_coord
    true_horizontal_coord = horizontal_coord % puzzle_width

    vertical_coord += vertical_adder
    horizontal_coord += horizontal_adder 

    return vertical_coord, horizontal_coord, puzzle_input[true_vertical_coord][true_horizontal_coord]


puzzle_input = load_input()
puzzle_width, puzzle_height = len(puzzle_input[0]), len(puzzle_input)

print(" -- Part 1 --")

vertical_adder, horizontal_adder = 1, 3
vertical_coord, horizontal_coord = 0, 0

tree_count = 0
while vertical_coord < puzzle_height:
    vertical_coord, horizontal_coord, tile = next_coords_and_character(vertical_coord, horizontal_coord)

    if tile == "#":
        tree_count += 1

print(tree_count)


print(" -- Part 2 --")

tree_count_list = []
for horizontal_adder, vertical_adder in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    vertical_coord, horizontal_coord = 0, 0
    tree_count = 0
    while vertical_coord < puzzle_height:
        vertical_coord, horizontal_coord, tile = next_coords_and_character(vertical_coord, horizontal_coord)

        if tile == "#":
            tree_count += 1

    tree_count_list.append(tree_count)

print(reduce(lambda x, y: x*y, tree_count_list))
