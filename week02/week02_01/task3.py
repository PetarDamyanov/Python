# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
	f=open(filename,"w+")
	for x in range(1,numbers):
		f.write("{0} ".format(randint(1,numbers)))
	f.close()

def main():
	arg=sys.argv
	generate_numbers(arg[1],int(arg[2]))

if __name__ == '__main__':
    main()