def to_digits(n=None):
    a = []
    if n is None:
        return a
    while n > 0:
        a.append(int(str(n / 10).split('.')[1]))
        n = n // 10
    a.reverse()
    return a

# print(to_digits(123))

# print(to_digits(99999))

# print(to_digits(123023))
