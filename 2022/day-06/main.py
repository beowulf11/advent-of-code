def load():
    with open("input-1.txt") as f:
        return f.readline()


marker_array = []
for i, c in enumerate(load()):
    marker_array.append(c)

    if len(marker_array) == 14:
        if len(set(marker_array)) == 14:
            print(i + 1)
            break
        else:
            marker_array.pop(0)
