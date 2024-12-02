def load_input():
    with open("input.txt") as file:
        return list(map(lambda x: (x[:3], int(x[4:])), file.readlines()))

class Stack:
    def __init__(self):
        self.stack = []

    def put(self, value):
        self.stack.append(value)

    def get(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

class Bootloader:
    def __init__(self):
        self.accumulator = 0
        self.instruction_index = 0
        self.runned_instructions = set()
        self.instructions = []

    def load_part_1(self):
        current_instruction = self.instructions[self.instruction_index]
        while current_instruction not in self.runned_instructions:
            self.runned_instructions.add(current_instruction)
            
            self.instruction_index, self.accumulator = self.execute_instruction(current_instruction, self.instruction_index, self.accumulator)

            current_instruction = self.instructions[self.instruction_index]

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def execute_instruction(self, instruction, instruction_index, accumulator):
        return instruction.execute(instruction_index, accumulator)

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def reset(self):
        self.accumulator = 0
        self.instruction_index = 0
        self.runned_instructions = set()

    def load_part_2(self):
        self.list_runned_instructions = []
        return self.part_2_recursion(0, 0)[1]

    def part_2_recursion(self, index, accumulator):
        current_instruction = self.instructions[index]
        self.list_runned_instructions.append(current_instruction)
        self.runned_instructions.add(current_instruction)

        new_instruction_index, new_accumulator = self.execute_instruction(current_instruction, index, accumulator)

        if new_instruction_index == len(self.instructions):
            return True, new_accumulator

        next_instruction = self.instructions[new_instruction_index]
        if next_instruction in self.runned_instructions:
            return False, 0

        is_terminal, terminal_value = self.part_2_recursion(new_instruction_index, new_accumulator)

        if is_terminal:
            return True, terminal_value

        if isinstance(current_instruction, Acc):
            self.runned_instructions.discard(current_instruction)
            return False, 0
        
        possible_instructions = []
        if isinstance(current_instruction, Jmp):
            possible_instructions.append(Nop(current_instruction.index, current_instruction.value))
        else:
            is_in_instruction_range = lambda jmp: jmp.value + index < len(self.instruction) and index + jmp.value >= 0
            jmp_top_range = min(abs(index + 1 + 9 - len(self.instructions)), 9)
            jmp_bottom_range = min(9, index)
            print(jmp_top_range, jmp_bottom_range)

            possible_next_instructions = map(lambda value: Jmp(current_instruction.index, value), range(-jmp_bottom_range, jmp_top_range + 1))
            possible_instructions.extend(list(filter(lambda instruction: not (instruction in self.runned_instructions and is_in_instruction_range(instruction)), possible_next_instructions)))

        for instruction in possible_instructions:
            new_instruction_index, new_accumulator = self.execute_instruction(instruction, index, accumulator)

            if new_instruction_index == len(self.instructions):
                print(instruction)
                return True, new_accumulator

            next_instruction = self.instructions[new_instruction_index]
            if next_instruction in self.runned_instructions:
                continue

            self.runned_instructions.add(instruction)
            is_terminal, terminal_value = self.part_2_recursion(new_instruction_index, new_accumulator)

            if is_terminal:
                print(instruction, "WTF")
                return True, terminal_value

            self.runned_instructions.discard(instruction)

        return False, 0


class Instruction:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __hash__(self):
        return self.index

class Acc(Instruction):
    def execute(self, instruction_index, accumulator):
        return instruction_index + 1, accumulator + self.value

    def __repr__(self):
        return f"[{self.index}] acc {self.value}"

class Nop(Instruction):
    def execute(self, instruction_index, accumulator):
        return instruction_index + 1, accumulator

    def __repr__(self):
        return f"[{self.index}] nop {self.value}"

class Jmp(Instruction):
    def execute(self, instruction_index, accumulator):
        return instruction_index + self.value, accumulator

    def __repr__(self):
        return f"[{self.index}] jmp {self.value}"

    
puzzle_input = load_input()

bootloader = Bootloader()
for index, tuple_instruction in enumerate(puzzle_input):
    instruction = None

    name, value = tuple_instruction
    if name == "acc":
        instruction = Acc(index, value)
    if name == "jmp":
        instruction = Jmp(index, value)
    if name == "nop":
        instruction = Nop(index, value)

    bootloader.add_instruction(instruction)

print(" -- Part 1 --")

bootloader.load_part_1()
print(bootloader.accumulator)

print(" -- Part 2 --")
bootloader.reset()
print(bootloader.load_part_2())
