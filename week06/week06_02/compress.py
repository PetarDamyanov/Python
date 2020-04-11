def compress(iterable, mask):
    for item in range(0, len(mask)):
        if mask[item]:
            value = yield iterable[item]