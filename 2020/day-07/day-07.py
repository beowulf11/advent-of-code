def load_input():
    with open("input.txt") as file:
        return list(map(lambda x: x[:-2], file.readlines()))

puzzle_input = load_input()

class Bag:
    def __init__(self, bag_name):
        self.bag_name = bag_name
        self.children = dict()
        self.parents = set()

    def add_parent(self, bag_requirements):
        self.parents.add(bag_requirements)

    def add_child(self, count, bag_requirements):
        self.children[bag_requirements] = (count, bag_requirements)

    def __hash__(self):
        return hash(self.bag_name)
    
    def __repr__(self):
        children = " | ".join(map(lambda bag: bag[1].bag_name, self.children))
        parents = " | ".join(map(lambda bag: bag.bag_name, self.parents))
        return f"{self.bag_name} -- children = [{children}] parents = [{parents}]"


parsed_bag_list = []
for line in puzzle_input:
    bag, bag_requirements_string = line.split(" contain ")
    bag = " ".join(bag[:-1].split(" ")[:-1])

    bag_requirements = []
    if "no other bags" not in bag_requirements_string:
        bag_requirements = list(map(lambda x: " ".join(x.split(" ")[:-1]), bag_requirements_string.split(", ")))

    parsed_bag_list.append((bag, bag_requirements))

bag_dict = {}
for parsed_bag in parsed_bag_list:
    bag_dict[parsed_bag[0]] = Bag(parsed_bag[0])

for parsed_bag in parsed_bag_list:
    for bag_requirement in parsed_bag[1]:
        bag_dict[parsed_bag[0]].add_child(int(bag_requirement[:2]), bag_dict[bag_requirement[2:]])
        bag_dict[bag_requirement[2:]].add_parent(bag_dict[parsed_bag[0]])


print(" -- Part 1 --")

def get_parent_count(bag, required_bag_set):
    required_bag_set |= set(bag.parents)
    for parent_bag in bag.parents:
        get_parent_count(parent_bag, required_bag_set)

    return required_bag_set

required_bag_set = set()
get_parent_count(bag_dict["shiny gold"], required_bag_set)
print(len(required_bag_set))


print(" -- Part 2 --")

def get_child_and_count(bag):
    children_bags_partial_count = sum(map(lambda bag_tuple: bag_tuple[0], bag.children.values()))
    for child_count, child in bag.children.values():
        children_bags_partial_count += child_count * get_child_and_count(child)

    return children_bags_partial_count

print(get_child_and_count(bag_dict["shiny gold"]))
