from fractions import Fraction

def simplify_fraction(fraction):
	n=fraction[0]
	d=fraction[1]
	return str(Fraction(n,d))

def main():
	print(simplify_fraction((3,9)))
	print(simplify_fraction((1,7)))
	print(simplify_fraction((4,10)))
	print(simplify_fraction((462,63)))


if __name__ == '__main__':
	main()