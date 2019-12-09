from time import time

class Plant:
    def __init__(self, index, left_distance=None, left=None, right=None):
        self.left_dist = left_distance
        self.left = left
        self.right = right
        self.index = index

    def around(self):
        if self.left is None and self.right is None:
            return "..#.."

        left = ".."
        if self.left and self.left_dist < 3:
            left = ".#"
            if self.left_dist == 2:
                left = "#."
            elif self.left.left and self.left.left_dist < 2:
                left = "##"

        right = ".."
        if self.right and self.right.left_dist < 3:
            right = "#."
            if self.right.left_dist == 2:
                right = ".#"
            elif self.right.right and self.right.right.left_dist < 2:
                right = "##"

        return left + "#" + right

    def __repr__(self):
        return str(self.index)

def around(index, room_state):
    left = ".."
    if index - 1 in room_state and index - 2 in room_state:
        left = "##"
    elif index - 1 in room_state:
        left = ".#"
    elif index - 2 in room_state:
        left = "#."

    right = ".."
    if index + 1 in room_state and index + 2 in room_state:
        right = "##"
    elif index + 1 in room_state:
        right = "#."
    elif index + 2 in room_state:
        right = ".#"

    if index in room_state:
        return left + "#" + right
    return left + "." + right

def next_iteration():
    global rules, room_state, curr_zero

    s = time()
    new_room_state = set()
    for x in room_state:
        for i in range(x - 1, x + 2):
            prvok = around(i, room_state)
            new_state = rules.get(prvok, ".")
            if new_state != ".":
                new_room_state.add(i)

    room_state = new_room_state
    #print(time() - s)

def eval(index, room_state, rules):
    prvok = room_state[index - 2:index + 3]
    next_state = rules.get("".join(prvok), ".")
    #print("Index =", index, "State =", room_state[index], "Next state =", next_state, "Prvok =", "".join(prvok))
    if next_state != room_state[index]:
        return next_state

    return None



if __name__ == "__main__":
    f = open("input.txt")
    room_state = set()
    line = f.readline()[15:-1]
    for x in range(len(line)):
        if line[x] == ".":
            continue
        room_state.add(x)


    f.readline()
    line = f.readline()[:-1]
    rules = dict()
    while line:
        rule, output = line.split(" => ")
        rules[rule] = output
        line = f.readline()[:-1]
    f.close()

    vypis = 50000
    for x in range(50000000000):
        if x % vypis == 0:
            print(x)
        next_iteration()

    print(sum(x for x in room_state))

    print(room_state)

    if False:
        vypis = 5000
        curr_zero = 3
        begin_shift, end_shift = 0, 0
        for x in range(1, 50000000000 + 1):
            if x == 1000:
                pass
                #print("".join(room_state), begin_shift, end_shift, "".join(room_state[begin_shift:]))
            if x % vypis == 0:
                print(x)
            begin_shift, end_shift = next_iteration(begin_shift, end_shift)
        value = 0
        for x in range(len(room_state)):
            if room_state[x] == "#":
                value += x - curr_zero
        print(value)
