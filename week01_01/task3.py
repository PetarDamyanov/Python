def to_number(n):
	s=""
	for x in n:
	#	print(x)
		s+=str(x)
	return int(s)

print(to_number([1,2,3]))

print(to_number([9,9,9,9,9]))

print(to_number([1,2,3,0,2,3]))

print(to_number([21, 2, 33]))

