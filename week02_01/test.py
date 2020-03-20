import sys
def t(arg):
	print(len(arg))
	for x in str(arg).split(" "):
		print(x)

n=[]
n=sys.argv
t(n)