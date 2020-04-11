def group(arugment):
    # arugment.sort()
    l_sort = []
    l_helper = []
    for x in range(0, len(arugment) - 1):
        l_helper.append(arugment[x])
        if x == len(arugment):
            l_sort.append(l_helper)
        if arugment[x] != arugment[x + 1]:
            l_sort.append(l_helper)
            l_helper = []
    l_helper.append(arugment[len(arugment) - 1])
    l_sort.append(l_helper)
    return l_sort

phone_dict = {0: " ", 1: "Up", 2: "a", 22: "b", 222: "c",
    3: "d", 33: "e", 333: "f",
    4: "g", 44: "h", 444: "i",
    5: "j", 55: "k", 555: "l",
    6: "m", 66: "n", 666: "o",
    7: "p", 77: "q", 777: "r", 7777: "s",
    8: "t", 88: "u", 888: "v",
    9: "w", 99: "x", 999: "y", 9999: "z"
    }


def numbers_to_message(pressed_sequence):
    str_list = []
    s = ""
    for x in pressed_sequence:
        s += (str(x))

    str_list = s.split("-1")

    list_split = []

    l_group = []

    for x in str_list:
        list_help = []
        for y in x:
            list_help.append(y)
        list_split.append(list_help)
    for x in list_split:
        l_group.append(group(x))
    for x in l_group:
    print(l_group)
    print(list_split)

numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
# "abc"
numbers_to_message([2, 2, 2, 2])
# "a"
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
# "Ivo e Panda"