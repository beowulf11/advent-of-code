def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class PC:
    def __init__(self):
        self.cycles = 0
        self.x = 1
        self.signal_sum = 0
        self.current_instruction = None
        self.current_arguments = None
        self.rows = [[" " for _ in range(40)] for _ in range(7)]

    def process_instruction(self, instruction, args):
        self.current_instruction = instruction
        self.current_arguments = args
        if instruction == "noop":
            self.tick()
        else:
            self.tick(2)

    def tick(self, count=1):
        # print(f"Start cycle\t\t{self.cycles + 1}: begin executing {self.current_instruction}, {self.current_arguments}")
        for i in range(count):
            self.cycles += 1
            if (self.cycles - 20) % 40 == 0:
                self.signal_sum += self.signal_strength()
            self.draw(self.cycles, self.x)
            # if i != count - 1:
                # print()

        if len(self.current_arguments) != 0:
            # print(self.x, self.current_arguments)
            self.x += int(self.current_arguments[0])
        # print(f"End of cycle {self.cycles}: finish executing {self.current_instruction}, {self.current_arguments} (Register X is now {self.x})")
        # sprite = ["." for _ in range(40)]
        # sprite[(self.x % 40) - 1] = "#"
        # sprite[self.x % 40] = "#"
        # sprite[(self.x % 40) + 1] = "#"
        # print(f"Sprite position: {''.join(sprite)}")
        # print()

    def draw(self, cycle, x):
        draw_x = x % 40
        draw_cycle = cycle % 40
        # print(f"DX: {draw_x}, DC: {draw_cycle}, X: {x}, C: {cycle}, A: {draw_x - 1 <= draw_cycle}, B: {draw_cycle <= draw_x + 1}", end=" -- ")
        if draw_x <= draw_cycle <= draw_x + 2:
            self.rows[(cycle - 1) // 40][draw_cycle - 1] = "#"
        else:
            self.rows[(cycle - 1) // 40][draw_cycle - 1] = "."

        # print(f"During cycle\t{cycle}: CRT draws pixel in position {draw_cycle - 1}")
        # print(draw_x, draw_cycle, " - ", draw_x - 1, draw_x + 1)
        # print(f"Current CRT row\t :{''.join(self.rows[cycle//40])}")
        #
        # print()

        ## Start cycle   1: begin executing addx 15
        ## During cycle  1: CRT draws pixel in position 0
        ## Current CRT row: #


    def signal_strength(self):
        return self.cycles * self.x

    def __repr__(self):
        return f"Cycles: {self.cycles}, X: {self.x}"



pc = PC()
for line in load():
    instruction, *args = line.split(" ")
    pc.process_instruction(instruction, args)

for r in pc.rows:
    print("".join(r))
print(pc.signal_sum)