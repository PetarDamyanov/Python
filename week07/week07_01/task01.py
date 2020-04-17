from contextlib import contextmanager


class Silence_Exception:

    def __init__(self, err, msg=None):
        self.err = err
        self.msg = msg

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        if self.err is type:
            if self.msg is None or self.msg is str(value):
                return True


@contextmanager
def silence_exception(err, msg=None):
    try:
        yield
    except err as e:
        if str(e) == msg or msg is None:
            pass
        else:
            raise e

# with Silence_Exception(ValueError):
#     # nothing should happen
#     raise ValueError('Test')

# with Silence_Exception(ValueError):
#     # the error should be re-raised since it is not expected.
#     raise TypeError('Test')

# with Silence_Exception(ValueError, 'Test'):
#     # nothing should happen
#     raise ValueError('Test')

# with Silence_Exception(ValueError, 'Testing.'):
#     # the error should be re-raised since it is not expected.
#     raise ValueError('Test')

# with silence_exception(ValueError):
#     # nothing should happen
#     raise ValueError('Test')

# with silence_exception(ValueError):
#     # the error should be re-raised since it is not expected.
#     raise TypeError('Test')

# with silence_exception(ValueError, 'Test'):
#     # nothing should happen
#     raise ValueError('Test')

# with silence_exception(ValueError, 'Testing.'):
#     # the error should be re-raised since it is not expected.
#     raise ValueError('Test')
