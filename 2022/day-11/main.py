from math import lcm


def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Monkey:
    def __init__(self, index, items, operation_line, test_line, result, monkeys):
        self.index = index
        self.items = items
        self.test_divider = int(test_line.split("by ")[1])
        self.test = lambda x: x % self.test_divider == 0
        self.lcm = 0
        self.result = result
        self.monkeys = monkeys

        self.inspected_count = 0

        if operation_line.count("old") == 2:
            self.operation = lambda x: (x*x) % self.lcm
        elif "*" in operation_line:
            num = int(operation_line.split("* ")[1])
            self.operation = lambda x: (x * num) % self.lcm
        else:
            num = int(operation_line.split("+ ")[1])
            self.operation = lambda x: (x + num) % self.lcm

    def turn(self, level):
        for item in self.items:
            self.inspected_count += 1
            level = self.worry_level(item, level)
            self.monkeys[self.result[self.test(level)]].items.append(level)
        self.items = []

    def worry_level(self, item, level):
        if level == 1:  # Part 1
            return self.operation(item) // 3
        else:  # Part 2
            return self.operation(item)

    def __repr__(self):
        return f"Monkey {self.index}:\t {', '.join(map(lambda x: str(x), self.items))}"


monkeys = []
lines = list(load())
for i, line in enumerate(lines[::7]):
    monkeys.append(Monkey(
       i,
       list(map(lambda x: int(x), lines[i*7 + 1].split(": ")[1].split(", "))),
       lines[i*7+2].split("= ")[1],
       lines[i*7+3],
       {1: int(lines[i*7+4].split("monkey ")[1]), 0: int(lines[i*7+5].split("monkey ")[1])},
       monkeys,
    ))

monkey_lcm = lcm(*list(map(lambda m: m.test_divider, monkeys)))
for m in monkeys:
    m.lcm = monkey_lcm


# #  Part 1 NO WORKING
# for i in range(1, 20):
#     for m in monkeys:
#         m.turn(1)
#
# sm = sorted(map(lambda m: m.inspected_count, monkeys), reverse=True)
# print(sm[0] * sm[1])

#  Part 2
for i in range(1, 10001):
    for m in monkeys:
        m.turn(2)

sm = sorted(map(lambda m: m.inspected_count, monkeys), reverse=True)
print(sm[0] * sm[1])
