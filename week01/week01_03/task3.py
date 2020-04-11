def goldbach(n):
	l=[2]
	res=[]
	for num in range(1,n+1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
				else:
					if l.count(num)==0:
						l.append(num)
	used=[]
	for x in l:
		if used.count(x)==0:
			
			if l.count(n-x)==1:
			
				used.append(n-x)
				res.append((x,n-x))
	# res=list(dict.fromkeys(res))
	print(res)
goldbach(4)
goldbach(6)
goldbach(8)
goldbach(10)
goldbach(100)