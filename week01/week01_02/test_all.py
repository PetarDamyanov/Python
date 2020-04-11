import unittest
from task1 import gas_stations
from task2 import is_number_balanced
from task3 import increasing_or_decreasing
from task5 import sum_of_numbers
from task6 import birthday_ranges


class Test_task1(unittest.TestCase):
    def test_task1_1(self):
        res = gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
        exp = [80, 140, 220, 290]
        self.assertEqual(res, exp)

    def test_task1_2(self):
        res = gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
        exp = [70, 140, 210, 280, 350, 350]
        self.assertEqual(res, exp)


class Test_task2(unittest.TestCase):
    def test_task2_1(self):
        res = is_number_balanced(9)
        self.assertTrue(res)

    def test_task2_2(self):
        res = is_number_balanced(4518)
        self.assertTrue(res)

    def test_task2_3(self):
        res = is_number_balanced(28471)
        self.assertFalse(res)

    def test_task2_4(self):
        res = is_number_balanced(1238033)
        self.assertTrue(res)


class Test_task3(unittest.TestCase):
    def test_task3_1(self):
        res = increasing_or_decreasing([1, 2, 3, 4, 5])
        self.assertEqual(res, "Up !")

    def test_task3_2(self):
        res = increasing_or_decreasing([5, 6, -10])
        self.assertFalse(res)

    def test_task3_3(self):
        res = increasing_or_decreasing([1, 1, 1, 1])
        self.assertFalse(res)

    def test_task3_4(self):
        res = increasing_or_decreasing([9, 8, 7, 6])
        self.assertEqual(res, "Down !")


class Test_task5(unittest.TestCase):

    def test_task5_1(self):
        res = sum_of_numbers("ab125cd3")
        self.assertEqual(res, 128)

    def test_task5_2(self):
        res = sum_of_numbers("ab12")
        self.assertEqual(res, 12)

    def test_task5_3(self):
        res = sum_of_numbers("ab")
        self.assertEqual(res, 0)

    def test_task5_4(self):
        res = sum_of_numbers("1101")
        self.assertEqual(res, 1101)

    def test_task5_5(self):
        res = sum_of_numbers("1111O")
        self.assertEqual(res, 1111)

    def test_task5_6(self):
        res = sum_of_numbers("1abc33xyz22")
        self.assertEqual(res, 56)

    def test_task5_7(self):
        res = sum_of_numbers("0hfabnek")
        self.assertEqual(res, 0)


class Test_task6(unittest.TestCase):
    def test_task6_1(self):
        res = birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
        exp = [2, 3, 4, 5, 2]
        self.assertEqual(res, exp)

    def test_task6_2(self):
        res = birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
        exp = [5, 2, 0, 1]
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
