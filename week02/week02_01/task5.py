import sys
import os
from os.path import getsize
from hurry.filesize import size


def size_file(filename):
    # print(filename)
    s = 0
    for dirpath, dirnames, filenames in os.walk(filename):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                s += os.stat(fp).st_size
            print(fp)
    print(size(s))

    # for dirs in os.walk(filename):
    #   # sum(getsize(dirs))
    #   print(dirs)


def main():
    path = str(sys.argv[1])
    size_file(path)
    # os.path.stat(path)
    # print(path)
    # print(os.stat(path))


if __name__ == '__main__':
    main()
