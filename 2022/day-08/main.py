from functools import reduce


def load():
    with open("input-1.txt") as f:
        return map(lambda l: l[:-1], f.readlines())


class Forrest:
    def __init__(self, row_size):
        self.columns = []
        self.rows = [[] for _ in range(row_size)]

    def add_column(self, column):
        row_index = len(self.rows[0])
        self.columns.append([Tree(c, row_index, i, self) for i, c in enumerate(column)])
        for i, t in enumerate(self.columns[-1]):
            self.rows[i].append(t)

    def paths_to_check(self):
        yield [x for x in self.columns]
        yield [x[::-1] for x in self.columns]
        yield [x for x in self.rows]
        yield [x[::-1] for x in self.rows]

    def visible_outside(self):
        for x in self.columns:
            x[0].is_visible = True
            x[-1].is_visible = True
        for x in self.rows:
            x[0].is_visible = True
            x[-1].is_visible = True

    def tree_visibilities(self, row, column):
        yield self.columns[row][column - 1::-1]
        yield self.columns[row][column + 1::]
        yield self.rows[column][row - 1::-1]
        yield self.rows[column][row + 1:]

    def __repr__(self):
        return "\n".join(map(lambda c: str(c), self.columns))


class Tree:
    def __init__(self, height, row, column, forrest):
        self.height = height
        self.row = row
        self.column = column
        self.forrest = forrest
        self.is_visible = False
        self.scores = []
        self.score = 0

    def visibility(self):
        pass

    def __repr__(self):
        return str(self.height) + f"({self.row}, {self.column} - {self.score})"


def check_line(trees):
    max_height = trees[0].height
    for tree in trees:
        if tree.height > max_height:
            max_height = tree.height
            tree.is_visible = True


f = None
for l in load():
    if f is None:
        f = Forrest(len(l))
    f.add_column(l)

# Part 1
for paths in f.paths_to_check():
    for path in paths:
        check_line(path)
f.visible_outside()

visible = 0
for col in f.columns:
    for t in col:
        if t.is_visible:
            visible += 1
print(visible)

# Part 2
max_score = 0
for column in f.columns[1:-1]:
    for tree in column[1:-1]:
        for path in f.tree_visibilities(tree.row, tree.column):
            score = 0
            for tree_in_path in path:
                score += 1
                if tree_in_path.height >= tree.height:
                    break
            tree.scores.append(score)
        tree.score = reduce(lambda x, y: x * y, tree.scores, 1)
        if tree.score > max_score:
            max_score = tree.score
print(max_score)
