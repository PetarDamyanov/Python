def cycle(iterable):
    i = 0
    while i<5:
    # while True:
        for x in iterable:
            value = yield x
        i+=1
    # print(value)

for x in list(cycle(range(5))):
    print(x)