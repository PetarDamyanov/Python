def is_credit_card_valid(n):
	n=str(n)
	if len(n)%2==0:
		return False
	l=[]
	s=n[0]
	# l.append(int(n[0]))
	for i in range(1,len(n)):
		# print('{0} -> {1}'.format(i,n[i]))
		if i%2!=0:
			# l.append(int(n[i])*2)
			s+=str(int(n[i])*2)
		else:
			s+=str(int(n[i]))
			# l.append(int(n[i]))
	for i in range(0,len(s)):
		l.append(int(s[i]))

	# print(l)
	# print(sum(l))
	if sum(l)%10==0:
		return True
	else:
		return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))