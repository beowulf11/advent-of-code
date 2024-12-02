def load_input():
    with open("input.txt") as file:
        return list(map(lambda line: int(line[:-1]), file.readlines()))

puzzle_input = load_input()

print(" -- Part 1 --")

found = False
for index_line1 in range(len(puzzle_input) - 1):
    for index_line2 in range(index_line1, len(puzzle_input)):
        num1, num2 = puzzle_input[index_line1], puzzle_input[index_line2]
        if num1 + num2 == 2020:
            print(num1 * num2)
            found = True
            break

    if found:
        break

print("\n -- Part 2 --")

found = False
for index_line1 in range(len(puzzle_input) - 2):
    for index_line2 in range(index_line1, len(puzzle_input) - 1):
        for index_line3 in range(index_line2, len(puzzle_input)):
            num1, num2, num3 = puzzle_input[index_line1], puzzle_input[index_line2], puzzle_input[index_line3]
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                found = True
                break
        if found:
            break
    if found:
        break
