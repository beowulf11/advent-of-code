from functools import reduce

inputLine = []
with open("input.txt") as file:
    line = file.readline()
    while line:
        inputLine.append(line[:-1])
        line = file.readline()


dlzka = 2
counts = [0 for _ in range(dlzka)]
for line in inputLine:
    letters = dict()
    countsAdded = [True for _ in range(dlzka)]
    for c in line:
        letters[c] = 1 + letters.get(c, 0)
    for c in letters:
        if letters[c] == 2 and countsAdded[0]:
            countsAdded[0] = False
            counts[0] += 1
        if letters[c] == 3 and countsAdded[1]:
            countsAdded[1] = False
            counts[1] += 1

print(reduce((lambda x, y: x * y), counts))

def compare(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff == 1

for i in range(len(inputLine) - 1):
    fl = inputLine[i]
    for sl in inputLine[i + 1:]:
        if compare(fl, sl):
            print(fl, sl)
            break
