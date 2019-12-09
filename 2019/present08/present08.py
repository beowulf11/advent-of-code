from PIL import Image

stream = open("input.txt").readline()[:-1]
# stream = "0222112222120000"

x_d, y_d = 25, 6
# x_d, y_d = 2, 2

layers = []

x_n, y_n = 0, 0
layer = []
for digit in stream:
    digit = int(digit)
    if x_n == x_d:
        y_n += 1
        x_n = 0
    if y_n == y_d:
        y_n = 0
        layers.append(layer)
        layer = []
    layer.append(digit)

    x_n += 1

layers.append(layer)

final_image = [0 for _ in range(x_d * y_d)]

for i in range(x_d * y_d):
    for layer in layers:
        if layer[i] == 2:
            continue
        final_image[i] = layer[i]
        break

im2 = Image.new("1", (x_d, y_d))
im2.putdata(final_image)
im2.show()
