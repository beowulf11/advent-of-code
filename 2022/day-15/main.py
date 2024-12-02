def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Sensor:
    def __init__(self, _x, _y, beacon_x, beacon_y):
        self.x = int(_x)
        self.y = int(_y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.rows = {}

    def beacon_distance(self):
        return abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def edges(self):
        dis = self.beacon_distance()
        return (self.x, self.y-dis), (self.x+dis, self.y), (self.x, self.y+dis), (self.x-dis, self.y)

    def taken_positions_on_row_1(self, row):
        edges = self.edges()
        if min(map(lambda _: _[1], edges)) > row:
            return set()
        if max(map(lambda _: _[1], edges)) < row:
            return set()

        dis = min(row - edges[0][1], edges[2][1] - row)
        return set(map(lambda rx: (rx, row), range(self.x - dis, self.x + dis + 1)))

    def taken_positions_on_row_2(self, range_top, range_bottom):
        edges = self.edges()
        top = min(edges[0][1], range_top)
        bottom = max(edges[2][1], range_bottom)

        if top < range_bottom or bottom > range_top:
            return []

        for row in range(bottom, top+1):
            row_range = self.rows.get(row, [])
            dis = min(row - edges[0][1], edges[2][1] - row)
            start, end = self.x - dis, self.x + dis
            for r in row_range:


            self.rows[row] = row_range

        return set(map(lambda rx: (rx, row), range(self.x - dis, self.x + dis + 1)))

    def __repr__(self):
        return f"[x:{self.x}, y:{self.y} | B x:{self.beacon_x}, y:{self.beacon_y} | Dis {self.beacon_distance()}]"


sensors = []
for line in load():
    x = line[12:line.find(", ")]
    y = line[line.find(", ") + 4:line.find(": ")]
    beacon_line = line[line.find("beacon is at x")+15:]
    b_x = beacon_line[:beacon_line.find(", ")]
    b_y = beacon_line[beacon_line.find(", ") + 4:]
    sensors.append(Sensor(x, y, b_x, b_y))


row_occupied = set()
for sensor in sensors:
    row_occupied |= sensor.taken_positions_on_row_1(2000000)
for sensor in sensors:
    row_occupied.discard((sensor.beacon_x, sensor.beacon_y))

print(len(row_occupied))