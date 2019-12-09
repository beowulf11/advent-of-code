original_tape = list(map(lambda x: int(x), open("input.txt").readline()[:-1].split(",")))

def proces(index, tape):
    if tape[index] == 99:
        return False
    if tape[index] == 1:
        tape[tape[index + 3]] = tape[tape[index + 1]] + tape[tape[index + 2]]
    elif tape[index] == 2:
        tape[tape[index + 3]] = tape[tape[index + 1]] * tape[tape[index + 2]]
    return index + 4

def process_tape(tape):
    index = 0
    while True:
        index = proces(index, tape)
        if index == False:
            break
    return tape[0]

for verb in range(100):
    for noun in range(100):
        tape = original_tape[:]
        tape[1] = noun
        tape[2] = verb
        if process_tape(tape) == 19690720:
            print(noun, verb)
            break

