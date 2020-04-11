import unittest
from task1 import anagram
from task2 import is_credit_card_valid
from task3 import goldbach


class Test_task1(unittest.TestCase):
    def test_task1_1(self):
        res = anagram("bread", "beard")
        self.assertTrue(res)

    def test_task1_2(self):
        res = anagram("breasdad", "beard")
        self.assertFalse(res)


class Test_task2(unittest.TestCase):
    def test_task2_1(self):
        res = is_credit_card_valid(79927398713)
        self.assertTrue(res)

    def test_task2_2(self):
        res = is_credit_card_valid(79927398715)
        self.assertFalse(res)


class Test_task3(unittest.TestCase):
    def test_task3_1(self):
        res = goldbach(4)
        self.assertEqual(res, [(2, 2)])

    def test_task3_2(self):
        res = goldbach(6)
        self.assertEqual(res, [(3, 3)])

    def test_task3_3(self):
        res = goldbach(8)
        self.assertEqual(res, [(3, 5)])

    def test_task3_4(self):
        res = goldbach(10)
        self.assertEqual(res, [(3, 7), (5, 5)])

    # def test_tas3_5(self):
    #     res = goldbach(100)
    #     self.assertEqual(res, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])


if __name__ == '__main__':
    unittest.main()
