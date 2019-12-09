f = open("input.txt")
line = [int(x) for x in f.readline().split(' ')]
f.close()

class Point:
    def __init__(self, childrens):
        self.childCount = childrens
        self.children = []
        self.metadata = None

    def add_metadata(self, metadata):
        print(metadata)
        self.metadata = metadata

    def add_child(self, child):
        self.children.append(child)

    def evaulate(self):
        if self.childCount == 0:
            print(f"NO CHILDREN: {self.metadata}")
            return sum(self.metadata)
        value = 0
        childLen = len(self.children)
        print(childLen)
        print("Adding: ", end="")
        print(len(self.children))
        print(", ".join(str(x) if x <= childLen else "" for x in self.metadata))
        for x in self.metadata:
            if x > childLen:
                continue
            value += self.children[x - 1].evaulate()
        return value

    def calculate(self):
        return sum(self.metadata) + sum(x.calculate() for x in self.children)


points = []
metadata_sum = []
root = None

def add_point(index, parent):
    global root
    children = line[index]
    metadata = line[index+1]
    self = Point(children)
    if parent is None:
        root = self
    else:
        parent.add_child(self)
    new_index = index + 2
    for x in range(children):
        new_index = add_point(new_index, self) + 1
    if children > 0 and len(self.children) == 0:
        print("FAWD")
        pass
    self.add_metadata([x for x in line[new_index: new_index + metadata]])
    metadata_sum.append([x for x in line[new_index: new_index + metadata]])
    return new_index + metadata - 1

add_point(0, root)
print(root.evaulate())
print(root.calculate())
