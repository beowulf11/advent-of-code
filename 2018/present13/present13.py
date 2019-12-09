
class TrackMap:
    def __init__(self):
        self.tracks = dict()
        self.carts = []

    def addTrack(self, column, row, znak):
        self.tracks[(column, row)] = znak

    def addCart(self, column, row, dirrection):
        self.carts.append(Cart(column, row, dirrection))
        if dirrection == ">" or dirrection == "<":
            self.addTrack(column, row, "-")
        if dirrection == "^" or dirrection == "v":
            self.addTrack(column, row, "|")

    def correctTrack(self):
        '''TODO: pokial to nejde mozno je chyba v tom ze neberies na uvahy kedy sa davaju / a \\'''
        for cart in self.carts:
            x, y = cart.get_pos()
            top = self.tracks.get((x, y - 1))
            right = self.tracks.get((x + 1, y))
            down = self.tracks.get((x, y + 1))
            left = self.tracks.get((x - 1, y))
            if (top is not None and top != "-") and (left is None and left != "|") and (down is not None and down != "-") and (right is not None and right != "|"):
                self.addTrack(x, y, "+")
            elif (top is None or top == "-") and (down is None or down == "-"):
                self.addTrack(x, y, "-")
            elif (left is None or left == "|") and (right is None or right == "|"):
                self.addTrack(x, y, "|")

    def next(self, cart):
        new_pos = cart.new_move()
        if self.tracks.get(new_pos, None) is None:
            import pdb; pdb.set_trace()
        cart.move(self.tracks[new_pos])
        return new_pos

    def iter(self):
        self.carts.sort(key=lambda cart: (cart.y, cart.x))
        for x in self.carts:
            print(x.y, x.x)
        print()
        for cart in self.carts:
            print(cart)
            self.next(cart)
        print("-------------")
        collision = set()
        for c in self.carts:
            collision.add((c.x, c.y))
        if len(collision) != len(self.carts):
            return (cart.x, cart.y)
        return True


    def __repr__(self):
        mapa = []
        s = 0
        pred = None
        for track in self.tracks:
            if track[1] != s:
                s = track[1]
                pred = None
                mapa.append("\n")
            if pred is not None:
                mapa.append(" "*(track[0] - pred[0] - 1))
            else:
                mapa.append(" "*track[0])
            if track in self.carts:
                mapa.append("o")
            else:
                mapa.append(self.tracks[track][0])
            pred = track
        return "".join(mapa)


class Cart:
    def __init__(self, column, row, dirrection):
        self.x = column
        self.y = row
        self.rotation = 0
        self.dirr = 0
        self.history = []
        if dirrection == ">":
            self.dirr = 1
        if dirrection == "v":
            self.dirr = 2
        if dirrection == "<":
            self.dirr = 3
        #0 - up, 1 - right, 2 - down, 3 - left
        self.next_move = {0: lambda x, y: (x, y - 1), 1: lambda x, y: (x + 1, y), 2: lambda x, y: (x, y + 1), 3: lambda x, y: (x -1 , y)}

    def get_pos(self):
        return self.x, self.y

    def new_move(self):
        return self.next_move[self.dirr](self.x, self.y)

    def move(self, next_track):
        self.history.append((self.x, self.y, next_track, self.dirr))
        if next_track == "/":
            if self.dirr == 0:
                self.dirr = 1
                self.y -= 1
            elif self.dirr == 1:
                self.dirr = 0
                self.x += 1
            elif self.dirr == 2:
                self.dirr = 3
                self.y += 1
            else:
                self.dirr = 2
                self.x -= 1
            return
        if next_track == "\\":
            if self.dirr == 0:
                self.dirr = 3
                self.y -= 1
            elif self.dirr == 1:
                self.dirr = 2
                self.x += 1
            elif self.dirr == 2:
                self.dirr = 1
                self.y += 1
            else:
                self.dirr = 0
                self.x -= 1
            return
        if next_track == "+":
            self.x, self.y = self.new_move()
            self.dirr = (self.dirr + 3 + self.rotation) % 4
            self.rotation = (self.rotation + 1) % 4
        else:
            self.x, self.y = self.new_move()

    def __eq__(self, other):
        if type(other) == tuple:
            return self.x == other[0] and self.y == other[1]
        if self.dirr != other.dirr:
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y) + ", dirr = " + str(self.dirr)

if __name__ == "__main__":
    trackMap = TrackMap()
    with open("input.txt") as file:
        line = file.readline()
        row = 0
        while line:
            column = 0
            for c in line[:-1]:
                if c != " ":
                    if c not in ["<", "v", "^", ">"]:
                        trackMap.addTrack(column, row, c)
                    else:
                        print(column, row)
                        trackMap.addCart(column, row, c)
                column += 1
            line = file.readline()
            row += 1
    trackMap.correctTrack()
    iteracia = 0
    print()
    while True:
        print(iteracia)
        vysl = trackMap.iter()
        if vysl != True:
            break
        iteracia += 1
        break
    print(vysl)
    for x in trackMap.carts:
        print(x)
