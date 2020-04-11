import unittest
import json,xml
from panda import Panda
class TestJsoanble(unittest.TestCase):
	def test_josn_to_json(self):
		p=Panda("Gosgo")
		exp='{"name": "Gosgo", "type": "Panda"}'
		try:
			t=p.to_json()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)
	def test_josn_fomr_json(self):
		# p=Panda("Gosgo")
		t='{"name": "Gosgo", "type": "Panda"}'
		try:
			p=t.from_json()
		except Exception as e:
			raise e
		self.assertEqual(Panda("Pesho"),p)
class TestXmlable(unittest.TestCase):
	def test_cml_to_xml(self):
		p=Panda("Gosgo")
		exp='<Panda><name>Gosgo</name></Panda>'
		try:
			t=p.to_xml()
		except Exception as e:
			raise e
		self.assertEqual(t,exp)

if __name__ == '__main__':
	unittest.main()