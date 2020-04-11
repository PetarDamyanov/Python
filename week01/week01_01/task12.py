def group(arugment):
    arugment.sort()
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
