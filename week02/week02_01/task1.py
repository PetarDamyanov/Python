# cat.py
import sys


def cat(arguments):
    f = open(arguments, "r")
    for x in f.readlines():
        print(x)
    f.close()


def main():
    cat(str(sys.argv[1]))


if __name__ == '__main__':
    main()
