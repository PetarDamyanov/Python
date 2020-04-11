import unittest
from cycle import cycle


class test_cycle(unittest.TestCase):
    def test_cycle_list(self):
    	res = cycle(range(0, 10))
		for x in res:
			print(x)        

if __name__ == '__main__':
    unittest.main()