
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from cancellation_policy import (
    validate_conditions,
    ensure_conditions,
    pair_conditions,
    get_cancellation_policy,
    get_current_condition,
    sort_conditions
)


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
    def test_all_conditions_have_hours_after_ensuring(self):
        cond1 = {'hours': 10, 'percent': 10}
        cond2 = {'percent': 100}
        conditions = [cond1, cond2]

        ensure_conditions(conditions)

        self.assertEqual(cond1['hours'], 10)
        self.assertEqual(cond2['hours'], 0)


class TestPairConditions(unittest.TestCase):
    def test_pair_conditions_with_two_elements(self):
        conditions = [{'hours': 10, 'percent': 20}, {'hours': 0, 'percent': 50}]

        result = pair_conditions(conditions)

        expected = [({'hours': 10, 'percent': 20}, {'hours': 0, 'percent': 50})]
        self.assertEqual(result, expected)

    def test_pair_conditions_with_even_number_of_elements(self):
        conditions = [
            {'hours': 24, 'percent': 0},
            {'hours': 18, 'percent': 20},
            {'hours': 12, 'percent': 50},
            {'hours': 0, 'percent': 100}
        ]

        result = pair_conditions(conditions)

        expected = [
            ({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
            ({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
            ({'hours': 12, 'percent': 50}, {'hours': 0, 'percent': 100})
        ]

        self.assertEqual(result, expected)

    def test_pair_conditions_with_odd_number_of_elements(self):
        conditions = [
            {'hours': 24, 'percent': 0},
            {'hours': 18, 'percent': 20},
            {'hours': 12, 'percent': 50},
            {'hours': 6, 'percent': 80},
            {'hours': 0, 'percent': 100}
        ]

        result = pair_conditions(conditions)

        expected = [
            ({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
            ({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
            ({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
            ({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
        ]

        self.assertEqual(result, expected)


class TestGetCurrentCondition(unittest.TestCase):

    @patch('cancellation_policy.my_now', autospec=True)
    def test_with_current_date_before_min_condition_date_should_return_min_condition_percent(self, datetime_mock):
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        conditions = [
            ({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
            ({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
            ({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
            ({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
        ]
        booking_end = datetime_mock.now() - timedelta(hours=100)
        result = get_current_condition(conditions, booking_end)
        self.assertEqual(result, 0)

    @patch('cancellation_policy.my_now', autospec=True)
    def test_with_current_date_in_condition_interval_should_return_higher_condition_percent(self, datetime_mock):
        conditions = [
            ({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
            ({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
            ({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
            ({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
        ]
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=29)

        booking_start = datetime_mock.now() + timedelta(hours=10)
        # print(timedelta(hours=10))
        result = get_current_condition(conditions, booking_start)

        self.assertEqual(result, 80)

    @patch('cancellation_policy.my_now', autospec=True)
    def test_with_current_date_equal_to_condition_hours_should_return_interval_upper_boundary_percent(self, datetime_mock):
        conditions = [
            ({'hours': 24, 'percent': 0}, {'hours': 18, 'percent': 20}),
            ({'hours': 18, 'percent': 20}, {'hours': 12, 'percent': 50}),
            ({'hours': 12, 'percent': 50}, {'hours': 6, 'percent': 80}),
            ({'hours': 6, 'percent': 80}, {'hours': 0, 'percent': 100})
        ]
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        booking_end = datetime_mock.now() + timedelta(hours=6)

        result = get_current_condition(conditions, booking_end)

        self.assertEqual(result, 100)


class TestGetCancellationPolicy(unittest.TestCase):
    @patch('cancellation_policy.my_now', autospec=True)
    def test_with_now_equal_to_booking_start_should_raise_error(self, datetime_mock):
        conditions = [{'percent': 50}]
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        booking_end = datetime_mock.now()
        exc = None

        try:
            get_cancellation_policy(conditions, 10, booking_end)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid booking start.')

    @patch('cancellation_policy.my_now', autospec=True)
    def test_with_now_later_than_booking_start_should_raise_error(self, datetime_mock):
        conditions = [{'percent': 50}]
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        booking_end = datetime_mock.now() - timedelta(hours=1)
        # now = booking_start + timedelta(hours=1)
        exc = None

        try:
            get_cancellation_policy(conditions, 10, booking_end)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid booking start.')

    @patch('cancellation_policy.my_now', autospec=True)
    def test_cancellation_fee_with_only_one_condition(self, datetime_mock):
        conditions = [{'percent': 50}]
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        price = 100
        booking_end = datetime_mock.now() + timedelta(hours=100)

        result = get_cancellation_policy(conditions, price, booking_end)

        self.assertEqual(result, 50.0)

    @patch('cancellation_policy.my_now', autospec=True)
    def test_cancellation_fee_with_several_conditions_and_now_in_them(self, datetime_mock):
        conditions = [
            {'hours': 24, 'percent': 10},
            {'hours': 12, 'percent': 50},
            {'hours': 6, 'percent': 80},
            {'percent': 100}
        ]
        price = 100
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        booking_end = datetime_mock.now() + timedelta(hours=10)

        result = get_cancellation_policy(conditions, price, booking_end)

        self.assertEqual(result, 80.0)

    @patch('cancellation_policy.my_now', autospec=True)
    def test_cancellation_fee_with_several_conditions_and_now_in_them_and_decimal_percent(self, datetime_mock):
        conditions = [
            {'hours': 24, 'percent': 10},
            {'hours': 12, 'percent': 50},
            {'hours': 6, 'percent': 65.5},
            {'percent': 100}
        ]
        price = 200
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        booking_end = datetime_mock.now() + timedelta(hours=10)

        result = get_cancellation_policy(conditions, price, booking_end)

        self.assertEqual(result, price * (65.5 / 100))


class TestSortConditions(unittest.TestCase):
    @patch('cancellation_policy.my_now', autospec=True)
    def test_conditions_are_sorted_in_descending_order(self, datetime_mock):
        conditions = [
            {'hours': 12, 'percent': 50},
            {'hours': 0, 'percent': 100},
            {'hours': 6, 'percent': 80},
            {'hours': 24, 'percent': 10},
        ]
        datetime_mock.now.return_value = datetime(2020, 4, 29)
        result = sort_conditions(conditions)

        expected = [
            {'hours': 24, 'percent': 10},
            {'hours': 12, 'percent': 50},
            {'hours': 6, 'percent': 80},
            {'hours': 0, 'percent': 100},
        ]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
