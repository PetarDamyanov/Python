from interface import *


def get_id():
    return input("add id:")


def get_user_info():
    full_name = input('full_name:')
    email = input('email:')
    age = int(input('age:'))
    phone = input('phone:')
    additional_info = input('additional_info:')
    return full_name, email, age, phone, additional_info


def menu(key):
    if key == 'a':
        full_name, email, age, phone, additional_info = get_user_info()
        add(full_name=full_name, email=email, age=age, phone=phone, additional_info=additional_info)
    elif key == 'l':
        list()
    elif key == 'd':
        delete(id=get_id())
    elif key == 'g':
        get(id=get_id())
    else:
        help()


def main():
    quit = True
    help()
    while quit:
        key_input = input('key:')
        if key_input == 'q':
            quit = False
        menu(key_input)


if __name__ == '__main__':
    main()
