import unittest
from decimal import *
from task02 import Change_precision,change_precision


class Test_Change_precision(unittest.TestCase):
    
    def test_change_percions_cls_1(self):
        with Change_precision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')  # 3.4
        exp = 3.4
        self.assertEqual(float(res), exp)

    def test_change_percions_cls_3(self):
        with Change_precision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')  # 3.4
        res2 = Decimal('2.31245')
        exp2 = 2.31245
        exp = 3.4
        self.assertEqual(float(res), exp)
        self.assertEqual(float(res2), exp2)


class Test_change_precision(unittest.TestCase):
    
    def test_change_percions_func_1(self):
        with change_precision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')  # 3.4
        exp = 3.4
        self.assertEqual(float(res), exp)

    def test_change_percions_func_3(self):
        with change_precision(2):
            res = Decimal('1.123132132') + Decimal('2.23232')  # 3.4
        res2 = Decimal('2.31245')
        exp2 = 2.31245
        exp = 3.4
        self.assertEqual(float(res), exp)
        self.assertEqual(float(res2), exp2)


if __name__ == '__main__':
    unittest.main()
