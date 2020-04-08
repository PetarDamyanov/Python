import time


def accepts(*args):

    function_args = args

    def inner(func):
        def print_type(*args):
            # print(function_args)
            for i in (0, len(args) - 1):
                    if type(args[i]) != function_args[i]:
                        raise TypeError("Argument {0} of {1} is not {2}!".format(args[i], func.__name__, function_args[i].__name__))
        return print_type
    return inner


# @accepts(str)
# def say_hello(name):
#     return "Hello, I am {}".format(name)


# say_hello(4)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))


deposit("Marto", 10)


def performance(file_name):
    file = open(file_name, "w")
    file = open(file_name, "a")

    def inner(method):
        def timed(*args, **kw):
            ts = time.time()
            method(*args, **kw)
            te = time.time()
            print(round(te - ts, 3))
            file.write(str(round(te - ts, 3)))
        return timed
        file.close()
    return inner


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


something_heavy()


def silence(file_name):
    file = open(file_name, "w")
    file = open(file_name, "a")

    def inner(method):
        def errors(*args, **kw):
            try:
                result=method(*args, **kw)
            except Exception as e:
                file.write(str(e))
                print(e)
        return errors
        file.close()
    return inner



@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')

foo(10)
foo(100)
