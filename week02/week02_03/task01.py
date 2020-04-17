def sort_uprising(iterable, key=None):
    t = type(iterable)
    if key is None:
        iterable = list(iterable)
        n = len(iterable)
        for i in range(n):
            for j in range(0, n - i - 1):
                if iterable[j] > iterable[j + 1]:
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    else:
        # print(iterable)
        for i in range(len(iterable) - 1):
            if iterable[i].get('age') > iterable[i + 1].get('age'):
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]

    return t(iterable)


def sort_downrising(iterable, key=None):
    t = type(iterable)
    if key is None:
        iterable = list(iterable)
        n = len(iterable)
        for i in range(n):
            for j in range(0, n - i - 1):
                if iterable[j] < iterable[j + 1]:
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    else:
        # print(iterable)
        for i in range(len(iterable) - 1):
            if iterable[i].get('age') < iterable[i + 1].get('age'):
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
    return t(iterable)


def my_sort(iterable, ascending=True, key=None):
    if len(iterable) == 0:
        return iterable
    if ascending is False:
        return sort_downrising(iterable, key)
    else:
        return sort_uprising(iterable, key)


def main():
    my_sort()


if __name__ == '__main__':
    main()
