from task01 import Jsonable,Xmlable
class Panda(Jsonable,Xmlable):
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return str(self.name)
	def __str__(self):
		return str(self.name)