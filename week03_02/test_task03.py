import unittest
from task03 import BowlingGame

class TestBowlingGame(unittest.TestCase):
	def test_bg_cls_only_strikes(self):
		game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
		exp=300
		
		try:
			t=game.result()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)

	def test_bg_cls_frames_only(self):
		game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
		exp=65
		try:
			t=game.result()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)

	def test_bg_cls_zero_only(self):
		game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
		exp=0
		try:
			t=game.result()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)

	def test_bg_cls_difrent_score(self):
		game = BowlingGame([1, 4, 10, 5, 2, 5, 5,
		 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
		exp=84
		try:
			t=game.result()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)







if __name__ == '__main__':
	unittest.main()