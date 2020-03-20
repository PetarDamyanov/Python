import unittest

from task1 import ensure_conditions
class TestEnsureConditions(unittest.TestCase):
    def test_ensure_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'hours':0,'percent': 100}
        ]

        ensure_conditions(conditions)

    def test_raises_exception_if_all_conditions_doesnt_have_hours(self):
        conditions = [
            {'percent': 10}
        ]
        exc = None

        # ACT
        try:
            ensure_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

if __name__ == '__main__':
	unittest.main()