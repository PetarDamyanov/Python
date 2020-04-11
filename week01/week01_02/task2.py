def is_number_balanced(number):
    if number > -9 and number < 9:
        return True
    num = str(number)
    half_len = int(len(num) / 2)
    n1 = list(num[-half_len::])
    n1_int = []
    n2 = list(num[:half_len:])
    n2_int = []
    for x in range(0, half_len):
        n1_int.append(int(n1[x]))
        n2_int.append(int(n2[x]))
    if sum(n1_int) == sum(n2_int):
        return True
    else:
        return False

print(is_number_balanced(9))

print(is_number_balanced(4518))

print(is_number_balanced(28471))

print(is_number_balanced(1238033))