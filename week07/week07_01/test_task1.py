import unittest
from task01 import Silence_Exception, silence_exception

class Test_Silence_Exeption(unittest.TestCase):

    def test_Silence_Exeption_1(self):
        with self.assertRaises(ValueError):
            with Silence_Exception(TypeError):
                raise ValueError('Test')

    def test_Silence_Exeption_2(self):
        with self.assertRaises(TypeError):
            with Silence_Exception(ValueError):
                raise TypeError()

    def test_Silence_Exeption_3(self):
        exception = None
        try:
            with Silence_Exception(ValueError, 'Test'):
                raise ValueError('Test')
        except Exception as e:
            exception = e
        self.assertIsNone(exception)

    def test_Silence_Exeption_4(self):
        with self.assertRaises(ValueError, msg='Raise'):
            with Silence_Exception(ValueError, 'Diffrent'):
                raise ValueError('Raise')


class Test_silence_exeption(unittest.TestCase):

    def test_silence_exeption_1(self):
        with self.assertRaises(ValueError):
            with silence_exception(TypeError):
                raise ValueError('Test')

    def test_silence_exeption_2(self):
        with self.assertRaises(TypeError):
            with silence_exception(ValueError):
                raise TypeError()

    def test_silence_exeption_3(self):
        exception = None
        try:
            with silence_exception(ValueError, 'Test'):
                raise ValueError('Test')
        except Exception as e:
            exception = e
        self.assertIsNone(exception)

    def test_silence_exeption_4(self):
        with self.assertRaises(ValueError, msg='Not'):
            with silence_exception(ValueError, 'Diffrent'):
                raise ValueError('Not')


if __name__ == '__main__':
    unittest.main()
