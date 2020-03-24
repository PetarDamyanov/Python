class F:
	a=5


class E: 
	b=1

class D: 
	c=2

class C(D, F): pass


class B(D, E): pass


class A(B, C): pass

from pprint import pprint
# pprint(A.mro())
pprint(locals()[E])