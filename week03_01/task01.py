from fractions import Fraction as fr
class CFractions():
	def __init__(self,n,d):
		self.n=n
		self.d=d
	def __str__(self):
		return "{0}/{1}".format(self.n,self.d)
	def simplify_fraction(self):
		return CFractions(fr(self.n,self.d).numerator,fr(self.n,self.d).denominator)
	def n_fraction():
		return fr(self.n,self.d).numerator
	def d_fractions():
		return fr(self.n,self.d).denominator
	def __repr__(self):
		return repr((self.n,self.d))
	def __add__(self,other):
		return CFractions(self.n+other.n,self.d+other.d)
	# def __eq__(self,other):
	# 	return self.n<other.n and self.d<other.d


class listFraction():
	def __init__(self,list):
		self.list=list
	def __repr__(self):
		s=""
		for x in self.list:
			s+="{0} ".format(x)
		return s	
	
	def sort_f(self):
		n=len(self.list)
		for i in range(n):
			for j in range(0, n-i-1):
				if self.list[j] > self.list[j+1]:
					self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
		return self.list




def collect_fractions(n1,n2): #list of fractions
	fNum=n1[0]*n2[1]+n2[0]*n1[1]
	sNum=n1[1]*n2[1]
	return CFractions(fNum,sNum).simplify_fraction()

def main():
	collect_fractions()


if __name__ == '__main__':
	main()