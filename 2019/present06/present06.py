class TreeNode():
    def __init__(self, name, children = None, parent = None):
        self.name = name
        self.parent = None
        self.children = [] if children is None else children

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        if self.children:
            return f"{self.name} -> {self.children}"
        return f"{self.name}"

orbit_list = [line[:-1].split(")") for line in open("input.txt").readlines()]
orbit_dict = dict()

for center, orbit in orbit_list:
    center_orbit = orbit_dict.get(center, TreeNode(center))
    orbit_orbit = orbit_dict.get(orbit, TreeNode(orbit))

    center_orbit.add_child(orbit_orbit)
    orbit_orbit.add_parent(center_orbit)

    orbit_dict[center_orbit.name] = center_orbit
    orbit_dict[orbit_orbit.name] = orbit_orbit

# pocet = 0
# 
# def count(node, c):
#     global pocet
#     pocet += c
#     c += 1
#     for child in node.children:
#         count(child, c)
# 
# count(orbit_dict["COM"], 0)

me = orbit_dict["YOU"]
visited = set()
neighbours = [me]

cycles = 0
found = False
while not found:
    new_neighbours = list()
    for neighbour in neighbours:
        if neighbour.name in visited:
            continue
        if neighbour.name == "SAN":
            found = True
        visited.add(neighbour.name)
        for new_neighbour in neighbour.children:
            if new_neighbour.name not in visited:
                new_neighbours.append(new_neighbour)
        if neighbour.parent is not None:
            new_neighbours.append(neighbour.parent)

    neighbours = new_neighbours

    cycles += 1


print(cycles - 3)
