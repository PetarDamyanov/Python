from decimal import *
from contextlib import contextmanager


class Change_precision:

    def __init__(self, num):
        self.num = num

    def __enter__(self):
        getcontext().prec = self.num

    def __exit__(self, type, value, traceback):
        getcontext().prec = 28


@contextmanager
def change_precision(num):
    getcontext().prec = num
    yield
    getcontext().prec = 28
