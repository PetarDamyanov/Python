def char_histogram(n):
    d = {}
    for i in n:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    return d


# char_histogram("Python!")

# char_histogram("AAAAaaa!!!")
