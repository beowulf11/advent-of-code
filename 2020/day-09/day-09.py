def load_input():
    with open("input.txt") as file:
        return list(map(lambda x: int(x[:-1]), file.readlines()))

puzzle_input = load_input()

def generate_possible_sums(number_list):
    possible_sums = set()
    for i, a in enumerate(number_list[:-1]):
        for b in number_list[i+1:]:
            possible_sums.add(a + b)

    return possible_sums


print(" -- Part 1 --")

preambule_length = 25
number_list = puzzle_input[:preambule_length]
index = preambule_length

invalid_number = None

while True:
    possible_sums = generate_possible_sums(number_list)
    element = puzzle_input[index]

    if element not in possible_sums:
        invalid_number = element
        break

    number_list.pop(0)
    number_list.append(element)
    index += 1

print(invalid_number)

print("\n -- Part 2 --")

processed_number_list = []
current_sum = 0
for number in puzzle_input:
    processed_number_list.append(current_sum + number)
    current_sum += number

range_start_index = None
range_end_index = None
partial_sum = None
for index in range(len(puzzle_input) - 1):
    partial_sum = puzzle_input[index]
    for inside_index in range(index + 1, len(puzzle_input)):
        partial_sum += puzzle_input[inside_index]
        if partial_sum == invalid_number:
            range_start_index = index
            range_end_index = inside_index
        
print(min(puzzle_input[range_start_index:range_end_index + 1]) + max(puzzle_input[range_start_index:range_end_index + 1]))
