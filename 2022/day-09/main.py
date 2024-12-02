def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Rope:
    def __init__(self, x, y, name, head=None):
        self.x = x
        self.y = y
        self.name = name
        self.head = head
        self.tail = None
        self.previous_move = None

        if head is not None:
            head.tail = self

    def is_close(self, other_rope):
        if abs(self.x - other_rope.x) > 1:
            return False
        elif abs(self.y - other_rope.y) > 1:
            return False
        return True

    def catch_up(self):
        if self.head is None or self.is_close(self.head):
            return

        if self.x == self.head.x and abs(self.y - self.head.y) == 2:
            self.previous_move = [0, clamp(self.head.y - self.y, -1, 1)]
        elif self.y == self.head.y and abs(self.x - self.head.x) == 2:
            self.previous_move = [clamp(self.head.x - self.x, -1, 1), 0]
        elif abs(self.x - self.head.x) + abs(self.y - self.head.y) > 2:
            self.previous_move = [
                clamp(self.head.x - self.x, -1, 1),
                clamp(self.head.y - self.y, -1, 1),
            ]
        else:
            self.previous_move = [
                (self.head.x - self.head.previous_move[0]) - self.x,
                (self.head.y - self.head.previous_move[1]) - self.y,
            ]

        self.x += self.previous_move[0]
        self.y += self.previous_move[1]

        visited.add((tail.x, tail.y))
        if self.tail is not None:
            self.tail.catch_up()

    def move(self, move_command):
        direction, move_count = move_command
        position_diff = (0, -1)  # UP
        if direction == "D":
            position_diff = (0, 1)  # DOWN
        elif direction == "L":
            position_diff = (-1, 0)  # LEFT
        elif direction == "R":
            position_diff = (1, 0)  # RIGHT

        self.previous_move = position_diff
        for _ in range(int(move_count)):
            self.x += position_diff[0]
            self.y += position_diff[1]
            self.tail.catch_up()

    def __repr__(self):
        return f"{self.name} [{self.x}, {self.y}]"


def print_board(head):
    board = [["_" for _ in range(-14, 13)] for _ in range(-14, 13)]
    ropes = []
    current_rope = head
    while current_rope is not None:
        ropes.append(current_rope)
        current_rope = current_rope.tail

    for row, line in enumerate(board):
        for column, _ in enumerate(line):
            printed = False
            for rope in ropes:
                if rope.x == column - 11 and rope.y == row - 11:
                    print(rope.name, end="")
                    printed = True
                    break
            if not printed:
                print("_", end="")
        print()


def clamp(num, min_v, max_v):
    return min(max_v, max(min_v, num))


# Part 1
visited = set()
visited.add((0, 0))
head = Rope(0, 0, "H")
tail = Rope(0, 0, "T", head)
for line in load():
    head.move(line.split(" "))

print(len(visited))

# Part 2
visited = set()
visited.add((0, 0))
head = Rope(0, 0, "H")
tail = None
previous_head = head
for i in range(1, 10):
    previous_head = Rope(0, 0, i, previous_head)
    tail = previous_head

for line in load():
    head.move(line.split(" "))

print(len(visited))
