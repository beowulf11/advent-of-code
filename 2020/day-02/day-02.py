def load_input():
    with open("input.txt") as file:
        return list(map(lambda line: parse_line(line), file.readlines()))

def parse_line(line):
    line = line[:-1]
    index_plist = line.rfind(" ")
    policy, password = line[:index_plist], line[index_plist + 1:]
    start, end = map(lambda num: int(num), policy[:policy.find(" ")].split("-"))
    char = policy[-2]
    return start, end, char, password

puzzle_input = load_input()

print(" -- Part 1 --")
count_correct_passwords = 0
for start, end, char, password in puzzle_input:
    occurence_guess = password.count(char)
    if not (occurence_guess < start or end < occurence_guess):
        count_correct_passwords += 1

print(count_correct_passwords)


print(" -- Part 2 --")
count_correct_passwords = 0
for start, end, char, password in puzzle_input:
    bool_first_occured = password[start - 1] == char
    bool_second_occured = password[end - 1] == char
    if bool_first_occured ^ bool_second_occured:
        count_correct_passwords += 1

print(count_correct_passwords)
