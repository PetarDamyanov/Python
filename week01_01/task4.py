from task2 import to_digits
def fact(n):
	sum=1
	for x in range(1,n+1):
			sum*=x
	return sum

# def to_digits(n):
# 	a=[]
# 	while n>0:
# 		a.append(int(str(n/10).split('.')[1]))
# 		n=n//10
# 	return a

def fact_digits(n):
	sum=0
	a=to_digits(n)
	for x in a:
		sum+=fact(x)
	return sum


# print(fact_digits(111))

# print(fact_digits(145))

# print(fact_digits(999))
