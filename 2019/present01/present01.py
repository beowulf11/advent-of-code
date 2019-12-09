from math import floor

planets = []
file = open("input.txt")
for line in file.readlines():
    planets.append(int(line[:-1]))
print(planets)

s = 0
for planet in planets:
    m = floor(planet / 3) - 2
    while m > 0:
        s += m
        m = floor(m / 3) - 2

print(s)
