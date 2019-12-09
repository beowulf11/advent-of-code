wires = list(map(lambda x: x[:-1], open("input.txt").readlines()))
wire1_turns = [x for x in wires[0].split(",")]
wire2_turns = [x for x in wires[1].split(",")]

# wire1_turns = [x for x in "R8,U5,L5,D3".split(",")]
# wire2_turns = [x for x in "U7,R6,D4,L4".split(",")]
# 
# wire1_turns = [x for x in "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")]
# wire2_turns = [x for x in "U62,R66,U55,R34,D71,R55,D58,R83".split(",")]

start = [0, 0]

wire1_pos = start[:]
wire1_points = dict()

wire2_pos = start[:]
wire2_points = dict()

def process_wire(wire_pos, wire_turns, wire_points):
    distance = 1
    for turn in wire_turns:
        distance = process_turn(wire_pos, turn, distance, wire_points)

def process_turn(position, turn, distance, points):
    direction = turn[0]
    if direction == "U":
        new_x = position[1] + int(turn[1:])
        for inter_pos in range(position[1] + 1, new_x + 1):
            p = (position[0], inter_pos)
            if p[0] == position[0] and p[1] == position[1]:
                pass
            else:
                if p not in points:
                    points[p] = distance
                distance += 1
        position[1] = new_x
    if direction == "R":
        new_y = position[0] + int(turn[1:])
        for inter_pos in range(position[0] + 1, new_y + 1):
            p = (inter_pos, position[1])
            if p[0] == position[0] and p[1] == position[1]:
                pass
            else:
                if p not in points:
                    points[p] = distance
                distance += 1
        position[0] = new_y
    if direction == "D":
        new_x = position[1] - int(turn[1:])
        for inter_pos in range(position[1], new_x - 1, -1):
            p = (position[0], inter_pos)
            if p[0] == position[0] and p[1] == position[1]:
                pass
            else:
                if p not in points:
                    points[p] = distance
                distance += 1
        position[1] = new_x
    if direction == "L":
        new_y = position[0] - int(turn[1:])
        for inter_pos in range(position[0], new_y - 1, -1):
            p = (inter_pos, position[1])
            if p[0] == position[0] and p[1] == position[1]:
                pass
            else:
                if p not in points:
                    points[p] = distance
                distance += 1
        position[0] = new_y
    return distance

process_wire(wire1_pos, wire1_turns, wire1_points)
process_wire(wire2_pos, wire2_turns, wire2_points)

min_distance = None
for point in (wire1_points.keys() & wire2_points.keys()):
    if point == (0, 0):
        continue
    new_distance = wire1_points[point] + wire2_points[point]
    if min_distance == None:
        min_distance = new_distance
    else:
        min_distance = min(min_distance, new_distance)
print(min_distance)
