def palindrome(n):
	n=str(n)
	nre=n[::-1]
	for i in range(0,len(n)-1):
		if n[i]==nre[i]:
			return True
		else:
			return False

'''

'''


# if palindrome(121):
# 	print("TRUE")
# else:
# 	print(FALSE)

# if palindrome("kapak"):
# 	print("TRUE")
# else:
# 	print("False")
# if palindrome("baba"):
# 	print("TRUE")
# else:
# 	print("FALSE")
