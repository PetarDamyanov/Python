from fractions import Fraction


def simplify_fraction(fraction):
    n = fraction[0]
    d = fraction[1]
    fractions = str(Fraction(n, d))
    f1 = fractions.split("/")[0]
    f2 = fractions.split("/")[1]
    return (int(f1), int(f2))


def main():
    pass


if __name__ == '__main__':
    main()
