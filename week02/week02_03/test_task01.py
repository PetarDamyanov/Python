import unittest
from task01 import my_sort, sort_uprising, sort_downrising


class Test_sort_uprising(unittest.TestCase):
    def test_uprisning_sort_normal_conditions_no_key(self):
        iterable = (10, 8, 9, 10, 100)
        correct = (8, 9, 10, 10, 100)
        try:
            iterable = sort_uprising(iterable)
        except Exception as e:
            raise e
        self.assertEqual(iterable, correct)

    def test_uprisning_sort_normal_conditions_with_key(self):
        iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        correct = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]
        try:
            iterable = sort_uprising(iterable, 'age')
        except Exception as e:
            raise e
        self.assertEqual(iterable, correct)


class Test_sort_downwising(unittest.TestCase):

    def Test_sort_downwising_normal_conditions_no_key(self):
        iterable = (10, 8, 9, 10, 100)
        correct = (100, 10, 10, 9, 8)
        try:
            iterable = sort_downrising(iterable)
        except Exception as e:
            raise e
        self.assertEqual(iterable, correct)

    def test_uprisning_sort_normal_conditions_with_key(self):
        iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        correct = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]
        try:
            iterable = sort_downrising(iterable, 'age')
        except Exception as e:
            raise e
        self.assertEqual(iterable, correct)


class test_my_sort(unittest.TestCase):
    def test_my_sort_empty_list(self):
        iterable = []
        correct = []
        try:
            my_sort(iterable)
        except Exception as e:
            raise e
        self.assertEqual(iterable, correct)


if __name__ == '__main__':
    unittest.main()
