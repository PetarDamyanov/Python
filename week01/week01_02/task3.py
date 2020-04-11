def increasing_or_decreasing(seq):
    i = 0
    j = 1
    flag = ""
    while j < len(seq):
        if (seq[j] - seq[i]) == 1:
            flag = "Up !"
        elif (seq[i] - seq[j]) == 1:
            flag = "Down !"
        else:
            return False
        i += 1
        j += 1
    return flag

print(increasing_or_decreasing([1,2,3,4,5]))

print(increasing_or_decreasing([5,6,-10]))

print(increasing_or_decreasing([1,1,1,1]))

print(increasing_or_decreasing([9,8,7,6]))
