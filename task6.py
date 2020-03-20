def count_vowels(n):
	cv=0
	n=n.lower()
	for x in n:
		#print(x)
		if x=="a" or x== "e" or x=="i" or x=="o" or x=="u" or x=="y":
			cv=cv+1
	print(cv)

count_vowels("Python")

count_vowels("Theistareykjarbunga") #It's a volcano name!

count_vowels("grrrrgh!")

count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")

count_vowels("A nice day to code!")