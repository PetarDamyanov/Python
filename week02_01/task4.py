# generate_numbers.py
import sys
from random import randint


def sum_num(filename):
	f=open(filename,"r")
	s=0
	for x in f.read().strip(" ").split(" "):
		s=s+int(x)
		# print(x)
	f.close()
	print(s)

def main():
	arg=sys.argv
	sum_num(arg[1])

if __name__ == '__main__':
    main()