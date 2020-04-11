import unittest
from compress import compress


class test_compress(unittest.TestCase):
    def test_compress_list(self):
        res = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
        exp = ["Panda"]
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
