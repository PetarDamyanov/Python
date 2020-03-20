import unittest
from task04 import my_sort,sort_uprising,sort_downrising

class Test_sort_uprising(unittest.TestCase):
	def test_uprisning_sort_normal_conditions_first(self):
		iterable=[(2, 3), (1, 2)]
		correct=[(1,2),(2,3)]
		try:
			iterable=sort_uprising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)
	def test_uprisning_sort_normal_conditions_second(self):
		iterable=[(2, 3), (1, 2), (1, 3)]
		correct=[(1,2),(1,3),(2,3)]
		try:
			iterable=sort_uprising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)
	
	def test_uprisning_sort_normal_conditions_third(self):
		iterable=[(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
		correct=[ (5, 6), (7, 8), (9, 6),(15, 32), (22, 7),(22, 78) ]
		try:
			iterable=sort_uprising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)
class Test_sort_downwising(unittest.TestCase):
	def test_downrisning_sort_normal_conditions_first(self):
		iterable=[(1, 2), (2, 3)]
		correct=[(2,3),(1,2)]
		try:
			iterable=sort_downrising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)
	def test_downrisning_sort_normal_conditions_second(self):
		iterable=[(2, 3), (1, 2), (1, 3)]
		correct=[(2,3),(1,3),(1,2)]
		try:
			iterable=sort_downrising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)
	
	def test_downrisning_sort_normal_conditions_third(self):
		iterable=[(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
		correct=[ (22, 78), (22, 7), (15, 32),(9, 6), (7, 8),(5, 6) ]
		try:
			iterable=sort_downrising(iterable)
		except Exception as e:
			raise e
		self.assertEqual(iterable,correct)



if __name__ == '__main__':
    unittest.main()