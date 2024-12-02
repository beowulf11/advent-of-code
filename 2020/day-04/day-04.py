all_lines = []
with open("input.txt") as file:
    passport = {}
    all_lines.extend(file.readlines())
    all_lines.append("")


print(" -- Part 1 --")

def first_part_is_password_correct(passport):
    required_fields_set = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    passport_set = passport.keys()
    return len(required_fields_set.difference(passport_set)) == 0

correct_passports = 0
for line in map(lambda line: line[:-1], all_lines):
    if line == "":
        is_correct_passports = first_part_is_password_correct(passport)
        if is_correct_passports:
            correct_passports += 1
        passport = {}
    else:
        for dict_item in line.split(" "):
            key, value = dict_item.split(":")
            passport[key] = value

print(correct_passports)


print(" -- Part 2 --")

def second_part_is_password_correct(passport):
    required_fields_set = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    passport_set = passport.keys()
    if len(required_fields_set.difference(passport_set)) != 0:
        return False

    if not digits_in_range(int(passport["byr"]), 1920, 2002):
        return False

    if not digits_in_range(int(passport["iyr"]), 2010, 2020):
        return False

    if not digits_in_range(int(passport["eyr"]), 2020, 2030):
        return False

    height, unit = int(passport["hgt"][:-2]), passport["hgt"][-2:]
    if unit == "cm":
        if not digits_in_range(height, 150, 193):
            return False
    elif unit == "in":
        if not digits_in_range(height, 59, 76):
            return False
    else:
        return False


    hair_color = passport["hcl"]
    valid_characters = set(range(10))
    valid_characters.update(set(("a", "b", "c", "d", "e", "f")))
    if hair_color[0] != "#" or len(hair_color) != 7 or set(map(lambda _: _, hair_color[1:])) > valid_characters:
        return False

    valid_characters = set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
    if passport["ecl"] not in valid_characters:
        return False

    pid = passport["pid"]
    if len(pid) != 9 or not pid.isnumeric():
        return False

    return True


def digits_in_range(digits, start, end):
    return start <= digits and digits <= end

correct_passports = 0
for line in map(lambda line: line[:-1], all_lines):
    if line == "":
        is_correct_passports = second_part_is_password_correct(passport)
        if is_correct_passports:
            correct_passports += 1
        passport = {}
    else:
        for dict_item in line.split(" "):
            key, value = dict_item.split(":")
            passport[key] = value

print(correct_passports)
