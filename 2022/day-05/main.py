import re


def load():
    with open("input-1.txt") as f:
        crate_lines = []
        move_lines = []
        is_moves = False
        for line in map(lambda l: l[:-1], f.readlines()):
            if is_moves:
                move_lines.append(line)
            elif line == "":
                is_moves = True
            else:
                crate_lines.append(line)

        return crate_lines, move_lines


class Stack:
    def __init__(self, index):
        self.index = index
        self.crates = []

    def move(self, other_stack, count):
        self.crates.extend(other_stack.remove_crates(count))

    def add(self, other_stack):
        self.crates.append(other_stack.remove_crate())

    def add_crate(self, crate, index=-1):
        self.crates.insert(index, crate)

    def remove_crates(self, count):
        popped = self.crates[-count:]
        [self.crates.pop() for _ in range(count)]
        return popped

    def remove_crate(self):
        return self.crates.pop()

    def __repr__(self):
        return f"crates={self.crates}"


crate_lines, move_lines = load()

num_of_rows = int(crate_lines[-1][crate_lines[-1].rfind(" "):])
stacks_1 = [Stack(i) for i in range(num_of_rows)]
for line in crate_lines[:-1]:
    indexes = [m.start() for m in re.finditer("\[", line)]
    for index in indexes:
        stack_index = index // 4
        crate = line[index + 1:line.find("]", index + 1)]
        stacks_1[stack_index].add_crate(crate, 0)

stacks_2 = [Stack(i) for i, _ in enumerate(stacks_1)]
for s in stacks_1:
    stacks_2[s.index].crates = s.crates.copy()

moves = []
for m in move_lines:
    sp = m.split(" ")
    moves.append((int(sp[1]), int(sp[3]), int(sp[5])))

# Part 1
#
# for move in moves:
#     for i in range(move[0]):
#         stacks_1[move[2] - 1].add(stacks_1[move[1] - 1])
#
# end = []
# for s in stacks_1:
#     end.append(s.crates[-1])
#
# print("".join(end))

# Part 2
for move in moves:
    stacks_2[move[2] - 1].move(stacks_2[move[1] - 1], move[0])

end = []
for s in stacks_2:
    end.append(s.crates[-1])

print("".join(end))
