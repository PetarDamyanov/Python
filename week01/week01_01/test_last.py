import unittest
from task11 import prime_factorization
from task12 import group
from task13 import max_consecutive


class Test_11(unittest.TestCase):

    def test_11_1(self):
        res = prime_factorization(10)
        exp = [(2, 1), (5, 1)]
        self.assertEqual(res, exp)

    def test_11_2(self):
        res = prime_factorization(14)
        exp = [(2, 1), (7, 1)]
        self.assertEqual(res, exp)

    def test_11_3(self):
        res = prime_factorization(356)
        exp = [(2, 2), (89, 1)]
        self.assertEqual(res, exp)

    def test_11_4(self):
        res = prime_factorization(89)
        exp = [(89, 1)]
        self.assertEqual(res, exp)

    def test_11_5(self):
        res = prime_factorization(1000)
        exp = [(2, 3), (125, 1)]
        self.assertEqual(res, exp)


class Test_12(unittest.TestCase):
    def test_12_1(self):
        res = group([1, 1, 1, 2, 3, 1, 1])
        exp = [[1, 1, 1, 1, 1], [2], [3]]
        self.assertEqual(res, exp)

    def test_12_2(self):
        res = group([1, 2, 1, 2, 3, 3])
        exp = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(res, exp)


class Test_13(unittest.TestCase):
    def test_13_1(self):
        res = max_consecutive([1, 2, 3, 3, 3, 3, 4, 3])
        exp = 4
        self.assertEqual(res, exp)

    def test_13_2(self):
        res = max_consecutive([1, 1, 2, 3, 3, 4, 4, 5, 5])
        exp = 2
        self.assertEqual(res, exp)

    def test_13_3(self):
        res = max_consecutive([1, 2, 3, 3, 3, 3, 4, 5])
        exp = 4
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
