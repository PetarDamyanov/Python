def nan_expand(n):
    s = ""
    for x in range(1, n + 1):
        s += "Not a "
    if n > 0:
        s += "NaN"
    else:
        s = ""
    return s

# nan_expand(0)

# nan_expand(1)

# nan_expand(2)

# nan_expand(3)
