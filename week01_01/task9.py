def sum_matrix(m):
	sum=0
	for i in m:
		#print(i)
		for j in i:
			sum+=j
	print(sum)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(m.len())
sum_matrix(m)

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_matrix(m)

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
sum_matrix(m)
