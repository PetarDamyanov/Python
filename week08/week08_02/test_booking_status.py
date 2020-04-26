import unittest
from unittest.mock import patch, Mock
from booking_status import get_booking_status
from datetime import datetime


class TestBookingStatus(unittest.TestCase):

    def test_booking_status_wtih_cancelled_mock(self):
        booking_mock = Mock(cancelled=True)
        self.assertEqual(get_booking_status(booking_mock), 'Cancelled')

    def test_booking_status_wtih_paid_mock(self):
        booking_mock = Mock(cancelled=False)
        booking_mock.is_fully_paid.return_value = True
        self.assertEqual(get_booking_status(booking_mock), 'Paid')

    @patch('booking_status.datetime', autospec=True)
    def test_booking_status_wtih_wait_mock(self, datetime_mock):
        booking_mock = Mock(cancelled=False, start=datetime(year=2020, month=1, day=1))
        booking_mock.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(3000, 4, 1)
        self.assertEqual(get_booking_status(booking_mock), 'Waiting taxes')

    @patch('booking_status.datetime', autospec=True)
    def test_booking_status_wtih_upcoming_mock(self, datetime_mock):
        booking_mock = Mock(cancelled=False, start=datetime(year=2020, month=1, day=1))
        booking_mock.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(2000, 4, 1)
        self.assertEqual(get_booking_status(booking_mock), 'Upcoming')


if __name__ == '__main__':
    unittest.main()
