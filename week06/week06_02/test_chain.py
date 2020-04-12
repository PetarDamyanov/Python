import unittest
from chain import chain


class test_chain(unittest.TestCase):
    def test_chain_list(self):
        res = chain(range(0, 4), range(4, 8))
        exp = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(list(res), exp)
        # print(type(res))


if __name__ == '__main__':
    unittest.main()
