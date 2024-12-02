def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def add_subdir(self, subdir):
        self.dirs.append(subdir)

    def add_file(self, f):
        self.files.append(f)

    def get_child_dir(self, name):
        child_dir = list(filter(lambda d: d.name == name, self.dirs))
        if len(child_dir) == 1:
            return child_dir[0]
        else:
            raise RuntimeError("More than 1 children, should not happen")

    def size(self):
        return sum(map(lambda f: f.size, self.files)) + sum(map(lambda d: d.size(), self.dirs))

    def str(self, depth):
        dir_size = self.size()
        repre = f"{'  ' * depth}- {self.name} (dir size:{dir_size})"
        for f in self.files:
            repre += f"\n{f.str(depth + 1)}"
        for d in self.dirs:
            repre += f"\n{d.str(depth + 1)}"
        return repre

    def __repr__(self):
        return self.str(0)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def str(self, depth):
        return f"{'  ' * depth}- {self.name} (file, size={self.size})"


root_dir = Dir("/")
current_dir = root_dir
for line in load():
    first, *rest = line.split(" ")
    if first == "ls":
        pass
    elif first == "$":
        if rest[0] == "ls":
            pass
        elif rest[0] == "cd":
            path = rest[1]
            if path == "/":
                current_dir = root_dir
            elif path == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child_dir(path)
    elif first == "dir":
        current_dir.add_subdir(Dir(rest[0], current_dir))
    else:
        current_dir.add_file(File(rest[0], int(first)))

# Part 1
dirs_meeting_threshold = []
def recurs(d):
    if d.size() <= 100000:
        dirs_meeting_threshold.append(d)
    for dd in d.dirs:
        recurs(dd)

recurs(root_dir)
print(sum(map(lambda d: d.size(), dirs_meeting_threshold)))

# Part 2
disk_size = 70000000
threshold_size = 30000000
30000000
27194032
42805968
total_size = root_dir.size()
unused_space = disk_size - total_size
need_remove_size = threshold_size - unused_space
print(need_remove_size)
print(f"unused_space: {unused_space}, used_size: {total_size}, need_remove_size: {need_remove_size}")

dirs = []
def recurs(d):
    dirs.append(d)
    for dd in d.dirs:
        recurs(dd)

recurs(root_dir)
bc = sorted(map(lambda d: d.size(), dirs))
print(bc)
for d in sorted(map(lambda d: d.size(), dirs)):
    print(d, d > need_remove_size)
    if d > need_remove_size:
        print(d)
        break
# print(list(filter(lambda d: d.size() > need_remove_size, dirs)))
