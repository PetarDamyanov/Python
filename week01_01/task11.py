def prime_factorization(n):
	ls=[]
	c=1
	while n%2==0:
		#print(n)
		c=c+1
		n=n//2
	ls.append({2,c})
	ls.append({n,1})
	print(ls)

prime_factorization(10)

prime_factorization(14)
prime_factorization(356)
prime_factorization(89)
prime_factorization(1000)
