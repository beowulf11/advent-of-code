drifts = []
with open("input.txt") as file:
    line = file.readline()
    while line:
        drifts.append(int(line[:-1]))
        line = file.readline()

freq = 0
repeatFreq = set()
search = True
while search:
    for d in drifts:
        repeatFreq.add(freq)
        freq += d
        if freq in repeatFreq:
            print(freq)
            print("Found")
            search = False
            break

print(freq)
