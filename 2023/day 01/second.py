def read(test: bool = False):
    lines = []
    with open("test2.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def parse_line(line: str) -> int:
    digit_set = digits.keys()
    first = None
    last = None
    first_digit_index = None
    last_digit_index = None

    for i, c in enumerate(line):
        try:
            n = int(c)
            if first is None:
                first = n
                first_digit_index = i
            last_digit_index = i
            last = n
        except ValueError:
            continue

    for digit in digit_set:
        index = line.find(digit)
        if index == -1:
            continue
        if first_digit_index is None or first_digit_index > index:
            first_digit_index = index
            first = digits[digit]

    for digit in digit_set:
        index = line.rfind(digit)
        if index == -1:
            continue
        if last_digit_index is None or last_digit_index < index:
            last_digit_index = index
            last = digits[digit]

    return first * 10 + last



lines = read(False)
result = []

for line in lines:
    result.append(parse_line(line))

print(sum(result))
