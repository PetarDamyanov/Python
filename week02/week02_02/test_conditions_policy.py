import unittest
from datetime import datetime,timedelta
from task1 import validate_conditions,ensure_conditions,group_conditions,get_current_condition,get_cancellation_fee


class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')

class TestEnsureConditions(unittest.TestCase):
    """docstring for TestEnsureConditions"""
    def test_ensure_conditions(self):
        conditions=[{'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        ensure_conditions(conditions)
        conditions2=[{'hours': 72, 'percent': 10000},
            {'hours':0,'percent': 10},
        ]
        
        self.assertEqual(conditions,conditions2)
class TestGroupConditions(unittest.TestCase):
    """docstring for TestGroupVonditions"""
    def test_group_conditions_normal(self):
        con = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours':0,'percent': 100}
        ]
        mat=[(24,12,10),(12,6,50),(6,0,80)]
        con=group_conditions(con)

        self.assertEqual(con,mat)

    def test_group_conditions_less(self):
        con = [
        {'hours': 24, 'percent': 10},
        {'hours': 6, 'percent': 80},
        {'hours':0,'percent': 100}
        ]
        mat=[(24,6,10),(6,0,80)]
        con=group_conditions(con)

        self.assertEqual(con,mat)
    def test_group_conditions_two(self):
        con = [
        {'hours': 24, 'percent': 10},
        {'hours':0,'percent': 100}
        ]
        mat=[(24,0,10)]
        con=group_conditions(con)

        self.assertEqual(con,mat)



class TestGetCurrentCondition(unittest.TestCase):
    """docstring for ClassName"""
    def test_get_current_condition_zero_hpurs(self):
        mat=[(24,12,10),(12,6,50),(6,0,80)]
        now = datetime.now()
        # start=now+timedelta(hours=10)
        start=now
        n = get_current_condition(mat,start,now)
        n1=100
        self.assertEqual(n,n1)
    def test_get_current_condition_above_24_hours(self):
        mat=[(24,12,10),(12,6,50),(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=24)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=10
        self.assertEqual(n,n1)

    def test_get_current_condition_for_10_hours(self):
        mat=[(24,12,10),(12,6,50),(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=10)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=50
        self.assertEqual(n,n1)
 


    def test_get_current_condition_zero_hpurs_less(self):
        mat=[(6,0,80)]
        now = datetime.now()
        # start=now+timedelta(hours=10)
        start=now
        n = get_current_condition(mat,start,now)
        n1=100
        self.assertEqual(n,n1)
    def test_get_current_condition_above_24_hours_less(self):
        mat=[(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=24)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=80
        self.assertEqual(n,n1)

    def test_get_current_condition_above_5_hours_less(self):
        mat=[(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=5)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=80
        self.assertEqual(n,n1)




    def test_get_current_condition_zero_hpurs_two(self):
        mat=[(12,6,50),(6,0,80)]
        now = datetime.now()
        # start=now+timedelta(hours=10)
        start=now
        n = get_current_condition(mat,start,now)
        n1=100
        self.assertEqual(n,n1)
    def test_get_current_condition_above_24_hours_two(self):
        mat=[(12,6,50),(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=24)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=50
        self.assertEqual(n,n1)

    def test_get_current_condition_above_5_hours_two(self):
        mat=[(12,6,50),(6,0,80)]
        now = datetime.now()
        start=now+timedelta(hours=5)
        # start=now
        n = get_current_condition(mat,start,now)
        n1=80
        self.assertEqual(n,n1)


class TestGetCancellationFee(unittest.TestCase):
    """docstring for Test"""
    def test_get_cancellation_fee_normal(self):
        percent=50
        price=1000
        ex=get_cancellation_fee(price,percent)
        ex2=500
        self.assertEqual(ex,ex2)
        
    def test_get_cancellation_fee_zero(self):
        percent=0
        price=1000
        ex=get_cancellation_fee(price,percent)
        ex2=0
        self.assertEqual(ex,ex2)
    def test_get_cancellation_fee_hundred(self):
        percent=100
        price=1000
        ex=get_cancellation_fee(price,percent)
        ex2=1000
        self.assertEqual(ex,ex2)
if __name__ == '__main__':
    unittest.main()