
def eval(x, y, serial):
    rackID = x + 10
    value = rackID * y + serial
    value *= rackID
    value = str(value)
    if len(value) > 2:
        return int(value[-3]) - 5
    return -5

def calculate(x, y, table, width):
    if y - width > 0 and x - width > 0:
        return table[y][x] - table[y-width][x] - table[y][x-width] + table[y-width][x-width]
    elif y - width > 0:
        return table[y][x] - table[y-width][x]
    elif x - width > 0:
        return table[y][x] - table[y][x-width]
    return table[y][x]

def biggest(x, y, table):
    biggest = 0
    biggest_w = None
    for width in range(1, min(x, y) + 2):
        new = calculate(x, y, table, width)
        if new > biggest:
            biggest = new
            biggest_w = width
    return biggest, biggest_w


def new_eval(x, y, serial, table):
    value = eval(x, y, serial)
    x -= 1
    y -= 1
    if y > 0 and x > 0:
        return value + table[y - 1][x] + table[y][x - 1] - table[y - 1][x - 1]
    elif y > 0:
        return value + table[y - 1][x]
    elif x > 0:
        return value + table[y][x - 1]
    else:
        return value

if "__main__" == __name__:
    serial = 4172
    w, h = 300, 300
    table = [[0 for x in range(1, w + 1)] for y in range(1, h + 1)]
    for y in range(h):
        for x in range(w):
            table[y][x] = new_eval(x + 1, y + 1, serial, table)
    m = 0
    coor = [0, 0, 0]
    for y in range(300):
        for x in range(300):
            new_s, new_h = biggest(x, y, table)
            if new_s > m:
                m = new_s
                coor[0], coor[1], coor[2] = x - new_h + 2, y - new_h + 2, new_h

    print(coor, m)
