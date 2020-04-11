import unittest

from task1 import group_conditions
class TestEnsureConditions(unittest.TestCase):
    def test_ensure_passes_with_valid_conditions(self):
        conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

        group_conditions(conditions)

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