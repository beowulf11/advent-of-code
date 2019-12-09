f = open("input.txt")
prereq = dict()
next_p = dict()
line = f.readline()[:-1]
dep, non_dep = set(), set()
while line:
    b, a = line[5], line[-12]
    dep.add(a)
    non_dep.add(b)

    pre = prereq.get(a, [])
    pre.append(b)
    prereq[a] = pre

    pre = next_p.get(b, [])
    pre.append(a)
    next_p[b] = pre

    line = f.readline()[:-1]
f.close()

path = []
workers = [None for x in range(5)]
considering = non_dep - dep

def get_next():
    min_p = None
    print(considering)
    for prvok in considering:
        if prvok not in prereq or all(x in path for x in prereq[prvok]):
            if min_p is None or min_p > prvok:
                min_p = prvok
    if min_p is None:
        return None
    considering.remove(min_p)
    return min_p

def assign(task):
    worker = None
    for x in range(len(workers)):
        if workers[x] is None:
            worker = x
            break
    workers[x] = [task, ord(task) - 64 + 60]

def work():
    for x in range(len(workers)):
        if workers[x] is not None:
            workers[x] = [workers[x][0], workers[x][1] - 1]

def end_work():
    for x in range(len(workers)):
        print(workers[x], end=", ")
        if workers[x] is not None and workers[x][1] == 0:
            path.append(workers[x][0])
            if workers[x][0] in next_p:
                considering.update(next_p[workers[x][0]])
            workers[x] = None
    print()

time = 0

while True:
    av_w = sum(1 if x is None else 0 for x in workers)
    if av_w == len(workers) and len(considering) == 0:
        break
    time += 1
    while True:
        if av_w == 0 or len(considering) == 0:
            break
        prvok = get_next()
        if prvok is None:
            break
        assign(prvok)
        av_w -= 1
    work()
    end_work()

print("".join(path), time)
