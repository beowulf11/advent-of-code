start, end = 147981, 691423

def is_increase(number_list):
    for i in range(len(number_list) - 1):
        if number_list[i] > number_list[i + 1]:
            return False
    return True

def is_twin(number):
    till_skip = None
    for i in range(len(number_list) - 1):
        if till_skip is not None and i < till_skip:
            continue
        if number_list[i] == number_list[i + 1]:
            if (i + 2 < len(number_list) and number_list[i] == number_list[i + 2]):
                till_skip = i + 3
                while till_skip < len(number_list) and number_list[i] == number_list[till_skip]:
                    till_skip += 1
            else:
                return True
    return False



# password = 112233
# number_list = list(int(x) for x in str(password))
# print(is_increase(number_list) and is_twin(number_list))
# password = 123444
# number_list = list(int(x) for x in str(password))
# print(is_increase(number_list) and is_twin(number_list))
# password = 111122
# number_list = list(int(x) for x in str(password))
# print(is_increase(number_list) and is_twin(number_list))
pocet = 0
for password in range(start, end + 1):
    number_list = list(int(x) for x in str(password))
    if is_increase(number_list) and is_twin(number_list):
        pocet += 1

print(pocet)
