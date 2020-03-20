def tf(n):
	if n:
		print("ANAGRAMS")
	else:
		print("NOT ANAGRAMS")
def anagram(s1,s2):
	if len(s1)!=len(s2):
		return False
	l1=[]
	l2=[]
	for i in range(0,len(s1)):
		l1.append(s1[i])
		l2.append(s2[i])
	l1.sort()
	l2.sort()
	# print('{0} => {1}'.format(l1,l2))
	if l1 == l2:
		return True
	else:
		return False

s=input()
tf(anagram(s.split(" ")[0],s.split(" ")[1]))