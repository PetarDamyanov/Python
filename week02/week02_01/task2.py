from task1 import cat
import sys


def main():
    arguments = sys.argv
    for x in range(1, len(arguments)):
        cat(str(arguments[x]))


if __name__ == '__main__':
    main()
