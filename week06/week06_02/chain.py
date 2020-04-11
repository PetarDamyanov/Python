def chain(iterable_one, iterable_two):
    for i in iterable_one:
        value = yield i
    for j in iterable_two:
        value = yield j
