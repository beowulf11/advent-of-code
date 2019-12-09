from queue import Queue
from itertools import permutations
from threading import Thread

original_tape = list(map(lambda x: int(x), open("input.txt").readline()[:-1].split(",")))
original_tape = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# print(original_tape)
original_tape.extend(list(x for x in range(500)))

def proces(index, base, input_tape, output_tape, tape):
    instruction = tape[index]

    op_code, index_shift, parameters = get_parameter_mode(instruction)

    if op_code == 99:
        return False, 0
    if op_code == 1:
        # 1, a, b, c <-> +(a, b) = c
        tape[value(tape, base, index + 3, parameters[2])] = value(tape, base, index + 1, parameters[0]) + value(tape, base, index + 2, parameters[1])
    elif op_code == 2:
        # 1, a, b, c <-> *(a, b) = c
        tape[value(tape, base, index + 3, parameters[2])] = value(tape, base, index + 1, parameters[0]) * value(tape, base, index + 2, parameters[1])
    elif op_code == 3:
        if input_tape.empty():
            print(f"instruction = {instruction}, base = {base}, index = {index}")
            raise Exception
        v = input_tape.get()
        # if instruction == 203:
        #     print(instruction, index, base, parameters, value(tape, base, index + 1, parameters[0]), v)
        tape[value(tape, base, index + 1, parameters[0])] = v
    elif op_code == 4:
        output = value(tape, base, index + 1, parameters[0])
        output_tape.put(output)
    elif op_code == 5:
        condition = value(tape, base, index + 1, parameters[0])
        if condition != 0:
            index_shift = 0
            index = value(tape, base, index + 2, parameters[1])
    elif op_code == 6:
        condition = value(tape, base, index + 1, parameters[0])
        if condition == 0:
            index_shift = 0
            index = value(tape, base, index + 2, parameters[1])
    elif op_code == 7:
        arg1, arg2 = value(tape, base, index + 1, parameters[0]), value(tape, base, index + 2, parameters[1])
        if arg1 < arg2:
            tape[value(tape, base, index + 3, parameters[2])] = 1
        else:
            tape[value(tape, base, index + 3, parameters[2])] = 0
    elif op_code == 8:
        arg1, arg2 = value(tape, base, index + 1, parameters[0]), value(tape, base, index + 2, parameters[1])
        if arg1 == arg2:
            tape[value(tape, base, index + 3, parameters[2])] = 1
        else:
            tape[value(tape, base, index + 3, parameters[2])] = 0
    elif op_code == 9:
        arg1 = value(tape, base, index + 1, parameters[0])
        # print(arg1, instruction, tape[index + 1], base, parameters)
        base += arg1

    return index + index_shift, base

def value(tape, base, tape_item_index, parameter):
    tape_item = int(tape[tape_item_index])
    if parameter == 0:
        return int(tape[tape_item])
    if parameter == 1:
        return int(tape_item)
    if parameter == 2:
        return int(tape[base + tape_item])

def get_parameter_mode(instruction):
    # the paramter modes are enterer in reversed order, 0-element is for 1 parameter, 1-element is for 2 parameter, ...
    code = instruction % 100
    instruction = str(int(instruction / 100))

    if code == 1: # 1 a b c < - > c = a + b
        return code, 4, parameter_append(instruction, 3)
    if code == 2: # 1 a b c < - > c = a + b
        return code, 4, parameter_append(instruction, 3)
    if code == 3: # 3 a < - > a = input()
        return code, 2, parameter_append(instruction, 1)
    if code == 4: # 4 a < - > output = a
        return code, 2, parameter_append(instruction, 1)
    if code == 5:
        return code, 3, parameter_append(instruction, 2)
    if code == 6:
        return code, 3, parameter_append(instruction, 2)
    if code == 7:
        return code, 4, parameter_append(instruction, 3)
    if code == 8:
        return code, 4, parameter_append(instruction, 3)
    if code == 9:
        return code, 2, parameter_append(instruction, 1)
    if code == 99:
        return code, 0, parameter_append(instruction, 0)

    print(f"code = {code}, instruction = {instruction}")
    raise Exception()


def parameter_append(instruction, length):
    return [int(mode) for mode in instruction[::-1] + "0" * (length - len(instruction))]

def process_tape(input_tape, output_tape, tape):
    index, base = 0, 0
    while True:
        index, base = proces(index, base, input_tape, output_tape, tape)
        if index == False:
            break

input_tape, output_tape = Queue(), Queue()
input_tape.put(1)
process_tape(input_tape, output_tape, original_tape)

while not output_tape.empty():
    print(output_tape.get())
