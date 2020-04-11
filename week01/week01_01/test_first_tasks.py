import unittest
from task1 import sum_of_digits
from task2 import to_digits
from task3 import to_number
from task4 import fact, fact_digits
from task5 import palindrome


class test_fist_task(unittest.TestCase):

    def test_task01_wtih_zero(self):
        res = sum_of_digits()
        exp = 0
        self.assertEqual(res, exp)

    def test_task01_wtih_less_than_zero(self):
        res = sum_of_digits(-10)
        exp = 1
        self.assertEqual(res, exp)

    def test_task01_wtih_normal(self):
        res = sum_of_digits(123)
        exp = 6
        self.assertEqual(res, exp)

    def test_whit_one_arg(self):
        res = sum_of_digits(6)
        exp = 6
        self.assertEqual(res, exp)


class test_second_task(unittest.TestCase):

    def test_second_task_normal(self):
        res = to_digits(123)
        exp = [1, 2, 3]
        self.assertEqual(res, exp)

    def test_second_task_empty(self):
        res = to_digits()
        exp = []
        self.assertEqual(res, exp)


class test_third_task(unittest.TestCase):

    def test_third_task_first(self):
        res = to_number([1, 2, 3])
        exp = 123
        self.assertEqual(res, exp)

    def test_third_task_second(self):
        res = to_number([21, 2, 33])
        exp = 21233
        self.assertEqual(res, exp)


class test_fourth_task(unittest.TestCase):

    def test_fourth_task_fact_zero(self):
        res = fact(0)
        exp = 1
        self.assertEqual(res, exp)

    def test_fourth_task_fact_normal(self):
        res = fact(5)
        exp = 120
        self.assertEqual(res, exp)

    def test_fourth_task_fact_digits(self):
        res = fact_digits(111)
        exp = 3
        self.assertEqual(res, exp)

    def test_fourth_task_fact_digits_second(self):
        res = fact_digits(145)
        exp = 145
        self.assertEqual(res, exp)

    def test_fourth_task_fact_digits_third(self):
        res = fact_digits(999)
        exp = 1088640
        self.assertEqual(res, exp)


class test_fifth_task(unittest.TestCase):

    def test_fifth_task_palidrome_number(self):
        res = palindrome(141)
        self.assertTrue(res)

    def test_fifth_task_palidrome_word(self):
        res = palindrome("kapak")
        self.assertTrue(res)

    def test_fifth_task_palidrome_word_false(self):
        res = palindrome("boza")
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
