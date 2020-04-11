import unittest
from task01 import Term,Polynomial
class TEstTerm(unittest.TestCase):
	"""docstring for TEstTerm"""
	def test_term_cls_siplify(self):
		t=Term('3x^3')
		ex='9x^2'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_c_only(self):
		t=Term('3')
		ex='0'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_x_no_c(self):
		t=Term('x^3')
		ex='3x^2'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_more(self):
		t=Term('10x^3')
		ex='30x^2'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_one(self):
		t=Term('3x^2')
		ex='6x'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_n_two_digits(self):
		t=Term('x^22')
		ex='22x^21'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)
	def test_term_cls_siplify_n_no(self):
		t=Term('x')
		ex='1'
		try:
			t=t.simplify()
		except Exception as e:
			raise e
		self.assertEqual(t,ex)


class TestPolinomial(unittest.TestCase):
	"""docstring for TestPolinomial"""
	def test_polinomial(self):
		p=Polynomial('x^4+10x^3')	
		self.assertEqual(['4x^3','30x^2'],p.spl())
	
	def test_polinomial_second(self):
		p=Polynomial('2x^3+x')
		self.assertEqual(['6x^2','1'],p.spl())


	def test_polinomial_third(self):
		p=Polynomial('1')
		self.assertEqual(['0'],p.spl())


	def test_polinomial_four(self):
		p=Polynomial('1+x^2')
		self.assertEqual(['0','2x'],p.spl())

	def test_polinomial_str_repr(self):
		p=Polynomial('1+x^2')
		try:
			p.spl()
		except Exception as e:
			raise e
		self.assertEqual("0+2x",str(p))


	def test_polinomial_str_repr_second(self):
		p=Polynomial('2x^3+x')
		try:
			p.spl()
		except Exception as e:
			raise e
		self.assertEqual("6x^2+1",str(p))


if __name__ == '__main__':
	unittest.main()