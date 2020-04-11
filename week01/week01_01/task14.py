
s="ivan"
srev=""
st=""
c=0
for x in range(len(s)-1,-1,-1):
	srev+=s[x]
nm="5 4"
arr=[["i", "v", "a", "n"],["e", "v", "n", "h"],["i", "n", "a", "v"],["m", "v", "v", "n"],["q" ,"r" ,"i" ,"t"]]
n=int(nm.split(" ")[0])
m=int(nm.split(" ")[1])
for x in arr:
	for y in x:
		st+=y
	# print(st)
	if s in st or srev in st:
		c=c+1
	st=""

for i in range(0,m,1):
	for j in range(0,n,1):
		st+=arr[j][i]
		# print(st)
	if s in st or srev in st:
		c=c+1
	st=""
'''
create string from list check if string or reverse string is in strign from array
'''		
'''
add input from keyboard
and maybe more tests
'''


		# print(arr[j][])

print(c)