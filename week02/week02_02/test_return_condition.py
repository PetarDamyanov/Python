import unittest

from task1 import get_current_condition
class TestGetCurrentConditions(unittest.TestCase):
    def test_get_current_coditoins_passes_with_valid_conditions(self):
        conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours': 0,'percent': 100}
    ]
        now = datetime.now()
        booking_start = now + timedelta(hours=10)
    

        get_current_condition(conditions,booking_start,now)

    def test_raises_exception_if_all_conditions_doesnt_have_hours(self):
        conditions = [
            {'percent': 10}
        ]
        exc = None

        # ACT
        try:
            group_conditions(conditions)
        except Exception as err:
            exc = err


        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')
    def test_raises_exception_if_all_conditions_have_hours_above_24(self):
        conditions = [
        {'hours': 214, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]
        exc = None

        # ACT
        try:
            group_conditions(conditions)
        except Exception as err:
            exc = err

    
        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

if __name__ == '__main__':
	unittest.main()