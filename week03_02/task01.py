class Term(object):
	"""docstring for Term"""
	def __init__(self, term):
		self.term=term
	def simplify(self):
		l=[]
		c=n=1
		if self.term=='x':
			self.term='1x'
		if self.term.count('x')==0:
			return '0'
		l=self.term.split('x')
		if l[1]=='':
			return '{0}'.format(l[0])
		else:
			if l[0].isdigit()==True:
				c=int(l[0])
			if l[len(l)-1].split('^')[1].isdigit():
				n=int(l[len(l)-1].split('^')[1])
		c*=n
		n-=1
		if n>=2:
			return '{0}x^{1}'.format(c,n)
		else:
			return '{0}x'.format(c)
	def __str__(self):
		return str(self.term)
	def __repr__(self):
		return str(self.term)
class Polynomial(object):
	"""docstring for Polynomial"""
	lst=[]
	def __init__(self, st=None):
		self.lst=[]
		if st!=None:
			for x in st.split("+"):
				self.lst.append(Term(x))
	def __len__(self):
		return len(self.lst)
	def spl(self):
		l=[]
		for x in self.lst:
			l.append(x.simplify())
		self.lst=l
		return l
	def __str__(self):
		s=""
		for x in self.lst:
			s+=str(x)
			if x!=self.lst[len(self.lst)-1]:
				s+="+"
		return s
	def __repr__(self):
		return self.lst