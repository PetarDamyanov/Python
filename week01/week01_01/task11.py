def prime_factorization(n):
    ls = []
    c = 0
    while n % 2 == 0:
        c += 1
        n = n // 2
    if c != 0:
        ls.append((2, c))
    ls.append((n, 1))
    return ls

# prime_factorization(10)

# prime_factorization(14)
# prime_factorization(356)
# prime_factorization(89)
# prime_factorization(1000)
