import unittest
from task01 import CFractions,collect_fractions
class test_fractions(unittest.TestCase):
	def test_str_fractions(self):
		# ,9fractions=(3,9)
		corect='3/9'

		try:
			t=str(CFractions(3,9))	
		except Exception as e:
			raise e
		self.assertEqual(t,corect)
	def test_simply_fr(self):
		corect='1,3'
		try:
			t=CFractions(3,9).simplify_fraction()
		except Exception as e:
			raise e
		self.assertEqual(t,corect)
class test_collect_fractions(unittest.TestCase):
	def test_collect_fractions(self):
		corect='3,4'
		try:
			t=collect_fractions((1, 4), (1, 2))
		except Exception as e:
			raise e
		self.assertEqual(t,corect)






if __name__ == '__main__':
	unittest.main()
		