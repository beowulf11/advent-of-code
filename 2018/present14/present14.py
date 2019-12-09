
class Cook:
    def __init__(self, ix, default):
        self.default = default
        self.ix = ix
        self.curr = default

    def __add__(self, cook):
        return self.curr + cook.curr

    def next(self, recepty):
        self.ix = (self.curr + 1 + self.ix ) % len(recepty)
        self.curr = recepty[self.ix]

    def __eq__(self, recipe):
        return self.default == recipe

recipes = [3, 7]
num_new = 2
c1, c2 = Cook(0, 3), Cook(1, 7)
record = 10
record_point = "430971"
record_recipes = ['3', '7']
while True:
    new_recipes = [int(x) for x in str(c1 + c2)]
    num_new += len(new_recipes)
    recipes.extend(new_recipes)
    if len(new_recipes) == 2:
        if len(record_recipes) >= len(record_point):
            record_recipes = record_recipes[1:]
        record_recipes.append(str(new_recipes[0]))
        if "".join(record_recipes) == record_point:
            break
        if len(record_recipes) >= len(record_point):
            record_recipes = record_recipes[1:]
        record_recipes.append(str(new_recipes[1]))
        if "".join(record_recipes) == record_point:
            break
    else:
        if len(record_recipes) >= len(record_point):
            record_recipes = record_recipes[1:]
        record_recipes.append(str(new_recipes[0]))
        if "".join(record_recipes) == record_point:
            break
    c1.next(recipes)
    c2.next(recipes)
print(num_new - len(record_point))
