from random import randrange


class Light:
    def __init__(self, x, y, delta_x, delta_y):
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y

    def next(self):
        self.x += self.delta_x
        self.y += self.delta_y
        return self.x, self.y

    def __repr__(self):
        return str(self.x) + " " +str(self.y)

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

def random_lights():
    f = randrange(0, len(lights))
    if f > len(lights) / 2:
        return lights[f], lights[randrange(0, f)]
    return lights[f], lights[randrange(f + 1, len(lights))]


f = open("input.txt")
line = f.readline()[:-1]
lights = []
while line:
    x = int(line[line.find('<') + 1: line.find(',')])
    y = int(line[line.find(',') + 1: line.find('>')])
    shift = line.find("y=<")
    delta_x = int(line[shift + 3: line.find(",", shift)])
    delta_y = int(line[line.find(",", shift) + 1:line.find(">", shift)])
    lights.append(Light(x, y, delta_x, delta_y))
    line = f.readline()[:-1]

def print_sky():
    shift_x = None
    shift_y = None
    max_x = None
    max_y = None
    for light in lights:
        if shift_x is None or shift_x > light.x:
            shift_x = light.x
        if shift_y is None or shift_y > light.y:
            shift_y = light.y
        if max_x is None or max_x < light.x:
            max_x = light.x
        if max_y is None or max_y < light.y:
            max_y = light.y
    width = abs(shift_x - max_x) + 1
    height = abs(shift_y - max_y) + 1
    screen = [['.' for _ in range(width)] for _ in range(height)]
    for light in lights:
        screen[light.y - shift_y][light.x - shift_x] = "#"
    for line in screen:
        print("".join(line))

sucet = 500
threshold = 20
iteracia = 0
min_sucet = None
while sucet > threshold:
    if iteracia % 500 == 0:
        print(iteracia, min_sucet)
        min_sucet = None
    iteracia += 1
    for light in lights:
        light.next()
    sucet = 0
    pocet = 50
    for _ in range(pocet):
        a, b = random_lights()
        sucet += a.dist(b)
    if sucet/pocet < threshold*1.5:
        print_sky()
        print(iteracia)
    sucet /= pocet
    if min_sucet is None or min_sucet > sucet:
        min_sucet = sucet

