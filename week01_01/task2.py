def to_digits(n):
	a=[]
	while n>0:
		a.append(int(str(n/10).split('.')[1]))
		n=n//10
		#print(n)
	return a

print(to_digits(123))

print(to_digits(99999))

print(to_digits(123023))



