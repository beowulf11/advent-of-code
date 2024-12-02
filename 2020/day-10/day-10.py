def load_input():
    with open("input.txt") as file:
        return list(map(lambda x: int(x[:-1]), file.readlines()))

puzzle_input = sorted(load_input())
puzzle_input.insert(0, 0)
puzzle_input.append(puzzle_input[-1] + 3)

differences = {}

index = 0
puzzle_lenght = len(puzzle_input)
while True:
    adapter = puzzle_input[index]

    first_difference = puzzle_input[index + 1] - adapter
    second_difference = 99 if index + 2 >= puzzle_lenght else puzzle_input[index + 2] - adapter
    third_difference = 99 if index + 3 >= puzzle_lenght else puzzle_input[index + 3] - adapter

    if first_difference <= 3:
        index += 1
        differences[first_difference] = differences.get(first_difference, 0) + 1

    elif index + 2 >= puzzle_lenght:
        break
    elif second_difference <= 3:
        index += 2
        differences[second_difference] = differences.get(second_difference, 0) + 1

    elif index + 3 >= puzzle_lenght:
        break
    elif third_difference <= 3:
        index += 3
        differences[third_difference] = differences.get(third_difference, 0) + 1

    if index >= puzzle_lenght - 1:
        break

print(differences[1] * differences[3])
