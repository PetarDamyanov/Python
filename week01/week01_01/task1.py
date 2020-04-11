def sum_of_digits(n=None):
	if n==None:
		return 0
	sum=0
	if n<0:
		n=n*-1
	while n>0:
		sum+=int(str(n/10).split('.')[1])
		n=n//10
		#print(n)
	return sum

# print(sum_of_digits(123))

# print(sum_of_digits(1325132435356))

# print(sum_of_digits(6))

# print(sum_of_digits(-10))
