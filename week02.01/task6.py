# generate_numbers.py
import sys
def count_file(filename,arg):
	f=open(filename,"r")
	c=0
	if arg=="char":
		c=len(f.read())
	elif arg=="word":
		s=f.read().split(" ")
		c=len(s)
	else:
		c=len(f.readlines())
	f.close()
	print("for {0} count:{1}".format(arg,c))

def main():
	arg=sys.argv
	for x in range(2,len(arg)):
		count_file(arg[1],arg[x])
if __name__ == '__main__':
    main()