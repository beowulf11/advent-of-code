def load_input():
    with open("input.txt") as file:
        return list(map(lambda line: line[:-1], file.readlines()))

def parse_seat_number(seat_code):
    row_code, column_code = seat_code[:7], seat_code[7:]

    row = binary_search(map(lambda x: 0 if x == "F" else 1, row_code), 0, 127)
    column = binary_search(map(lambda x: 0 if x == "L" else 1, column_code), 0, 7)

    return row * 8 + column

"""
    0 - Lower, 1 - Higher
"""
def binary_search(instructions, start_range, end_range):
    for instruction in instructions:
        diff = (end_range - start_range + 1) // 2
        if instruction == 0:
            end_range -= diff
        elif instruction == 1:
            start_range += diff

    return start_range


puzzle_input = load_input()

print(" -- Part 1 --")

print(max(map(lambda seat_code: parse_seat_number(seat_code), puzzle_input)))


print(" -- Part 2 --")

previous = None
for seat in sorted(map(lambda seat_code: parse_seat_number(seat_code), puzzle_input)):
    if previous is not None and seat - 1 != previous:
        break
    previous = seat

print(previous + 1)
