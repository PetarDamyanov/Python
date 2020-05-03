from client import *
from check_user import check
from mechanic import *


def print_hello():
    print('Hello!')
    return input('Provide user name:')


def main():
    exit = True
    user = print_hello()
    c_m, user_id = check(user)
    while exit:
        if c_m == 'c':
            choise = cleint_choise(user, user_id)
            if choise is False:
                exit = choise
        if c_m == 'm':
            choise = mechanic_choise(user, user_id)
            if choise is False:
                exit = choise


if __name__ == '__main__':
    main()
