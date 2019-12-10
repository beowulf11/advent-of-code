from queue import Queue
from itertools import permutations
from threading import Thread

original_tape = list(map(lambda x: int(x), open("input.txt").readline()[:-1].split(",")))
# original_tape = [104,1125899906842624,99]


class IntComputer:
    def __init__(self, tape, input_tape, output_tape):
        self.tape = tape
        self.input_tape = input_tape
        self.output_tape = output_tape
        self.index = 0
        self.base = 0
        self.outer = dict()

        self.halted = False

    def run(self):
        while not self.halted:
            self.step()

    def step(self):
        self.get_parameter_mode(self.get(self.index))

        if self.code == 99:
            self.halted = True
        elif self.code == 1:
            self.set(self.value_index(3), self.value(1) + self.value(2))
        elif self.code == 2:
            self.set(self.value_index(3), self.value(1) * self.value(2))
        elif self.code == 3:
            self.set(self.value_index(1), self.input_tape.get())
        elif self.code == 4:
            output_tape.put(self.value(1))
        elif self.code == 5:
            condition = self.value(1)
            if condition != 0:
                self.index_shift = 0
                self.index = self.value(2)
        elif self.code == 6:
            condition = self.value(1)
            if condition == 0:
                self.index_shift = 0
                self.index = self.value(2)
        elif self.code == 7:
            arg1, arg2 = self.value(1), self.value(2)
            if arg1 < arg2:
                self.set(self.value_index(3), 1)
            else:
                self.set(self.value_index(3), 0)
        elif self.code == 8:
            arg1, arg2 = self.value(1), self.value(2)
            if arg1 == arg2:
                self.set(self.value_index(3), 1)
            else:
                self.set(self.value_index(3), 0)
        elif self.code == 9:
            self.base += self.value(1)

        self.index += self.index_shift

    def get_parameter_mode(self, instruction):
        # the paramter modes are enterer in reversed order, 0-element is for 1 parameter, 1-element is for 2 parameter, ...
        self.code = instruction % 100
        self.index_shift = 0
        self.parameters = []

        instruction = str(int(instruction / 100))

        if self.code == 1: # 1 a b c < - > c = a + b
            self.index_shift = 4
        if self.code == 2: # 1 a b c < - > c = a + b
            self.index_shift = 4
        if self.code == 3: # 3 a < - > a = input()
            self.index_shift = 2
        if self.code == 4: # 4 a < - > output = a
            self.index_shift = 2
        if self.code == 5:
            self.index_shift = 3
        if self.code == 6:
            self.index_shift = 3
        if self.code == 7:
            self.index_shift = 4
        if self.code == 8:
            self.index_shift = 4
        if self.code == 9:
            self.index_shift = 2
        if self.code == 99:
            self.index_shift = 0
            return

        self.parse_parameters(instruction)

    def parse_parameters(self, instruction):
        self.parameters = [int(mode) for mode in instruction[::-1] + "0" * (self.index_shift - 1 - len(instruction))]

    def value_index(self, offset):
        parameter = self.parameters[offset - 1]

        if parameter == 0:
            return self.get(self.index + offset)
        elif parameter == 1:
            raise Exception
        elif parameter == 2:
            return self.base + self.get(self.index + offset)

    def value(self, offset):
        # offset = 0, is the instruction code, so the first value has offset of 1
        parameter = self.parameters[offset - 1]
        tape_item = self.get(self.index + offset)

        if parameter == 0:
            return self.get(tape_item)
        if parameter == 1:
            return tape_item
        if parameter == 2:
            return self.get(self.base + tape_item)

    def get(self, index):
        try:
            return self.tape[index]
        except:
            return self.outer.get(index, 0)

    def set(self, index, value):
        try:
            self.tape[index] = value
        except:
            self.outer[index] = value


input_tape, output_tape = Queue(), Queue()
input_tape.put(2)
pc = IntComputer(original_tape, input_tape, output_tape)
pc.run()


output = []
while not output_tape.empty():
    output.append(str(output_tape.get()))

print(", ".join(output))
