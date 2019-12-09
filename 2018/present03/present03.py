from functools import reduce

class Claim:
    def __init__(self, _id, _x, _y, _width, _height):
        self.valid = True
        self.id = _id
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height

    def populate(self, arr):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                if arr[y][x] == '.':
                    arr[y][x] = self.id
                else:
                    print(arr[y][x])
                    self.valid = False
                    claims[arr[y][x]].valid = False
                    arr[y][x] = self.id

def parse(cmd):
    firstS = cmd.find(" ")
    idB = int(cmd[1:firstS])
    xIndex = cmd.find(" ", firstS + 1)
    xCoor = int(cmd[xIndex + 1: cmd.find(",")])
    yIndex = cmd.find(":", xIndex + 1)
    yCoor = int(cmd[cmd.find(",") + 1: yIndex])
    w, h = [int(x) for x in cmd[yIndex + 2:].split("x")]
    return idB, xCoor, yCoor, w, h

claims = dict()
with open("input.txt") as file:
    line = file.readline()
    while line:
        cmd = parse(line[:-1])
        claims[cmd[0]] = Claim(*cmd)
        line = file.readline()

d = 2000
pole = [["." for _ in range(d)] for _ in range(d)]
for x in claims:
    claims[x].populate(pole)
print()
for p in claims:
    if claims[p].valid == True:
        print(p)
