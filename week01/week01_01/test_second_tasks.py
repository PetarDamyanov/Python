import unittest
from task6 import count_vowels
from task7 import count_consonants
from task8 import char_histogram
from task9 import sum_matrix
from task10 import nan_expand


class Test_Sixt_Task(unittest.TestCase):

    def test_sixt_task_first(self):
        res = count_vowels("Python")
        exp = 2
        self.assertEqual(res, exp)

    def test_sixt_task_second(self):
        res = count_vowels("Theistareykjarbunga")
        exp = 8
        self.assertEqual(res, exp)

    def test_sixt_task_third(self):
        res = count_vowels("grrrrgh!")
        exp = 0
        self.assertEqual(res, exp)

    def test_sixt_task_fourth(self):
        res = count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
        exp = 22
        self.assertEqual(res, exp)

    def test_sixt_task_fifth(self):
        res = count_vowels("A nice day to code!")
        exp = 8
        self.assertEqual(res, exp)


class Test_sevent_Task(unittest.TestCase):

    def test_sevent_task_first(self):
        res = count_consonants("Python")
        exp = 4
        self.assertEqual(res, exp)

    def test_sevent_task_second(self):
        res = count_consonants("Theistareykjarbunga")
        exp = 11
        self.assertEqual(res, exp)

    def test_sevent_task_third(self):
        res = count_consonants("grrrrgh!")
        exp = 7
        self.assertEqual(res, exp)

    def test_sevent_task_fourth(self):
        res = count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
        exp = 44
        self.assertEqual(res, exp)

    def test_sevent_task_fifth(self):
        res = count_consonants("A nice day to code!")
        exp = 6
        self.assertEqual(res, exp)


class Test_eight_task(unittest.TestCase):

    def test_eight_task_first(self):
        res = char_histogram("Python!")
        exp = {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}
        self.assertEqual(res, exp)

    def test_eight_task_second(self):
        res = char_histogram("AAAAaaa!!!")
        exp = {'A': 4, 'a': 3, '!': 3}
        self.assertEqual(res, exp)


class Test_nine_task(unittest.TestCase):

    def test_nine_task_first(self):
        res = sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        exp = 45
        self.assertEqual(res, exp)

    def test_nine_task_second(self):
        res = sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        exp = 0
        self.assertEqual(res, exp)


class Test_ten_task(unittest.TestCase):

    def test_ten_task_first(self):
        res = nan_expand(0)
        exp = ""
        self.assertEqual(res, exp)

    def test_ten_task_second(self):
        res = nan_expand(3)
        exp = "Not a Not a Not a NaN"
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
