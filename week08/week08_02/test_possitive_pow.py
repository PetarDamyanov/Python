import unittest
from unittest.mock import patch
from possitive_pow import big_possitive_pow


class TestPossitivePow(unittest.TestCase):
    @patch('possitive_pow.randint', autospec=True)
    def test_big_possitive_pow_with_mock_randint(self, randint_mock):
        randint_mock.return_value = 1
        self.assertEqual(big_possitive_pow(), 1)

    @patch('possitive_pow.randint', autospec=True)
    def test_big_possitive_pow_with_mock_randint_for_expetion(self, randint_mock):
        randint_mock.return_value = -1
        with self.assertRaises(ValueError, msg='Try again'):
            big_possitive_pow()

    @patch('possitive_pow.randint', autospec=True)
    def test_big_possitive_pow_with_mock_randint_for_expetion_with_zero(self, randint_mock):
        randint_mock.return_value = 0
        with self.assertRaises(ValueError, msg='Try again'):
            big_possitive_pow()

    @patch('possitive_pow.randint', autospec=True)
    def test_big_possitive_pow_with_mock_randint_check_x_equ_y(self, randint_mock):
        randint_mock.return_value = 2
        self.assertEqual(big_possitive_pow(), 4)


if __name__ == '__main__':
    unittest.main()
