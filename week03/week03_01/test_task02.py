import unittest
from task02 import Bill,BillBatch


class TestBillClass(unittest.TestCase):

    def test_bill_class_print_and_str(self):
        test = Bill(10)
        expected = "A 10$ bill"
        try:
            test = str(test)
        except Exception as e:
            raise e
        self.assertEqual(test, expected)

    def test_bill_class_negative_or_zero_numbers(self):
        test = Bill(-10)
        expected = "There is no zero or negative bills"
        try:
            test = str(test)
        except Exception as e:
            raise e
        self.assertEqual(test, expected)

    def test_bill_class_int_method(self):
        expected = type(4)
        try:
            test = Bill(10)
        except Exception as e:
            raise e
        self.assertEqual(type(int(test)), expected)

    def test_bill_not_equal(self):
        t1 = Bill(1)
        t2 = Bill(2)
        self.assertFalse(t1 == t2)

    def test_bill_equal(self):
        t1 = Bill(1)
        t2 = Bill(1)
        self.assertTrue(t1 == t2)

    def test_bill_class_hash_method_maybe(self):
        t1 = hash(Bill(5))
        t2 = hash(5)
        self.assertTrue(t1 == t2)

    def test_bill_class_add_method(self):
        t1 = Bill(5)
        t2 = Bill(5)
        self.assertTrue(t1 + t2 == 10)

    def test_bill_class_iadd_method(self):
        t1 = Bill(5)
        t2 = 5
        t1 += t2
        self.assertTrue(t1 == 10)


class Test_BillBatch(unittest.TestCase):

    def test_bill_batch_class_print(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        s = ""
        for bill in batch:
            s += bill
        expected = "A 10$ billA 20$ billA 50$ billA 100$ bill"
        self.assertEqual(s, expected)

    def test_bill_batch_class_len(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        self.assertEqual(len(batch), 4)

    def test_bill_batch_class_total(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        self.assertEqual(batch.total(), 180)


if __name__ == '__main__':
    unittest.main()
