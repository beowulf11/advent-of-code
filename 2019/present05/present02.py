from queue import Queue


tape = list(map(lambda x: int(x), open("input.txt").readline()[:-1].split(",")))
# tape = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

input_tape = Queue() # FIFO
output_tape = Queue() # FIFO

input_tape.put(5)

def proces(index):
    instruction = tape[index]

    op_code, index_shift, parameters = get_parameter_mode(instruction)

    if op_code == 99:
        return False
    if op_code == 1:
        # 1, a, b, c <-> +(a, b) = c
        tape[value(index + 3)] = value(index + 1, parameters[0]) + value(index + 2, parameters[1])
    elif op_code == 2:
        # 1, a, b, c <-> *(a, b) = c
        tape[value(index + 3)] = value(index + 1, parameters[0]) * value(index + 2, parameters[1])
    elif op_code == 3:
        tape[value(index + 1)] = input_tape.get()
    elif op_code == 4:
        output = value(index + 1, parameters[0])
        output_tape.put(output)
    elif op_code == 5:
        condition = value(index + 1, parameters[0])
        if condition != 0:
            index_shift = 0
            index = value(index + 2, parameters[1])
    elif op_code == 6:
        condition = value(index + 1, parameters[0])
        if condition == 0:
            index_shift = 0
            index = value(index + 2, parameters[1])
    elif op_code == 7:
        arg1, arg2 = value(index + 1, parameters[0]), value(index + 2, parameters[1])
        if arg1 < arg2:
            tape[value(index + 3)] = 1
        else:
            tape[value(index + 3)] = 0
    elif op_code == 8:
        arg1, arg2 = value(index + 1, parameters[0]), value(index + 2, parameters[1])
        if arg1 == arg2:
            tape[value(index + 3)] = 1
        else:
            tape[value(index + 3)] = 0

    return index + index_shift

def value(tape_item_index, parameter = 1):
    tape_item = int(tape[tape_item_index])
    if parameter == 0:
        return int(tape[tape_item])
    if parameter == 1:
        return int(tape_item)

def get_parameter_mode(instruction):
    # the paramter modes are enterer in reversed order, 0-element is for 1 parameter, 1-element is for 2 parameter, ...
    code = instruction % 100
    instruction = str(int(instruction / 100))

    if code == 1:
        return code, 4, parameter_append(instruction, 3)
    if code == 2:
        return code, 4, parameter_append(instruction, 3)
    if code == 3:
        return code, 2, parameter_append(instruction, 1)
    if code == 4:
        return code, 2, parameter_append(instruction, 1)
    if code == 5:
        return code, 3, parameter_append(instruction, 3)
    if code == 6:
        return code, 3, parameter_append(instruction, 3)
    if code == 7:
        return code, 4, parameter_append(instruction, 4)
    if code == 8:
        return code, 4, parameter_append(instruction, 4)
    if code == 99:
        return code, 0, parameter_append(instruction, 0)

    print(f"code = {code}, instruction = {instruction}")
    raise Exception()


def parameter_append(instruction, length):
    return [int(mode) for mode in instruction[::-1] + "0" * (length - len(instruction))]

def process_tape():
    index = 0
    while True:
        index = proces(index)
        if index == False:
            break
    return tape[0]

process_tape()

while not output_tape.empty():
    print(output_tape.get())

