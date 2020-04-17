def sort_uprising(iterable, key=None):
    iterable = list(iterable)
    n = len(iterable)
    for i in range(n):
        for j in range(0, n - i - 1):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    # print(iterable)
    return iterable


def sort_downrising(iterable, key=None):
    iterable = list(iterable)
    n = len(iterable)
    for i in range(n):
        for j in range(0, n - i - 1):
            if iterable[j] < iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]

    return iterable


def my_sort(iterable, ascending=True):
    if ascending is True:
        return sort_uprising(iterable)
    else:
        return sort_downrising(iterable)


def main():
    my_sort()


if __name__ == '__main__':
    main()
