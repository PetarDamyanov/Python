import unittest
from task02 import simplify_fraction


class Test_simplify_factions(unittest.TestCase):
    def test_simplify_factions_1(self):
        res = simplify_fraction((3, 9))
        exp = (1, 3)
        self.assertEqual(res, exp)

    def test_simplify_factions_2(self):
        res = simplify_fraction((1, 7))
        exp = (1, 7)
        self.assertEqual(res, exp)

    def test_simplify_factions_3(self):
        res = simplify_fraction((4, 10))
        exp = (2, 5)
        self.assertEqual(res, exp)

    def test_simplify_factions_4(self):
        res = simplify_fraction((462, 63))
        exp = (22, 3)
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
