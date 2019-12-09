from queue import Queue
from itertools import permutations
from threading import Thread

original_tape = list(map(lambda x: int(x), open("input.txt").readline()[:-1].split(",")))
# original_tape = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54, -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4, 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def proces(index, input_tape, output_tape, tape):
    instruction = tape[index]

    op_code, index_shift, parameters = get_parameter_mode(instruction)

    if op_code == 99:
        return False
    if op_code == 1:
        # 1, a, b, c <-> +(a, b) = c
        tape[value(tape, index + 3)] = value(tape, index + 1, parameters[0]) + value(tape, index + 2, parameters[1])
    elif op_code == 2:
        # 1, a, b, c <-> *(a, b) = c
        tape[value(tape, index + 3)] = value(tape, index + 1, parameters[0]) * value(tape, index + 2, parameters[1])
    elif op_code == 3:
        tape[value(tape, index + 1)] = input_tape.get()
    elif op_code == 4:
        output = value(tape, index + 1, parameters[0])
        output_tape.put(output)
    elif op_code == 5:
        condition = value(tape, index + 1, parameters[0])
        if condition != 0:
            index_shift = 0
            index = value(tape, index + 2, parameters[1])
    elif op_code == 6:
        condition = value(tape, index + 1, parameters[0])
        if condition == 0:
            index_shift = 0
            index = value(tape, index + 2, parameters[1])
    elif op_code == 7:
        arg1, arg2 = value(tape, index + 1, parameters[0]), value(tape, index + 2, parameters[1])
        if arg1 < arg2:
            tape[value(tape, index + 3)] = 1
        else:
            tape[value(tape, index + 3)] = 0
    elif op_code == 8:
        arg1, arg2 = value(tape, index + 1, parameters[0]), value(tape, index + 2, parameters[1])
        if arg1 == arg2:
            tape[value(tape, index + 3)] = 1
        else:
            tape[value(tape, index + 3)] = 0

    return index + index_shift

def value(tape, tape_item_index, parameter = 1):
    tape_item = int(tape[tape_item_index])
    if parameter == 0:
        return int(tape[tape_item])
    if parameter == 1:
        return int(tape_item)

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

def process_tape(input_tape, output_tape, tape):
    index = 0
    while True:
        index = proces(index, input_tape, output_tape, tape)
        if index == False:
            break
    return tape[0]

def amplifier_settings():
    amplifier = [5, 6, 7, 8, 9]
    for amp in permutations(amplifier):
        yield amp

def amplifier_unit(input_tape, output_tape, tape):
    process_tape(input_tape, output_tape, tape)

max_amplifier = 0
for amplifier in amplifier_settings():
    amp_a_input, amp_a_output = Queue(), Queue()
    amp_a_input.put(amplifier[0])
    amp_a_input.put(0)
    amp_a = Thread(target=amplifier_unit, args=(amp_a_input, amp_a_output, original_tape[:]), daemon=True)

    amp_b_output = Queue()
    amp_a_output.put(amplifier[1])
    amp_b = Thread(target=amplifier_unit, args=(amp_a_output, amp_b_output, original_tape[:]), daemon=True)

    amp_c_output = Queue()
    amp_b_output.put(amplifier[2])
    amp_c = Thread(target=amplifier_unit, args=(amp_b_output, amp_c_output, original_tape[:]), daemon=True)

    amp_d_output = Queue()
    amp_c_output.put(amplifier[3])
    amp_d = Thread(target=amplifier_unit, args=(amp_c_output, amp_d_output, original_tape[:]), daemon=True)

    amp_d_output.put(amplifier[4])
    amp_e = Thread(target=amplifier_unit, args=(amp_d_output, amp_a_input, original_tape[:]), daemon=True)

    amp_a.start()
    amp_b.start()
    amp_c.start()
    amp_d.start()
    amp_e.start()

    amp_a.join()
    amp_b.join()
    amp_c.join()
    amp_d.join()
    amp_e.join()

    o = amp_a_input.get()
    max_amplifier = max(max_amplifier, o)

print(max_amplifier)
