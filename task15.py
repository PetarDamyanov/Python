
def is_palindrome(word):
	return word== word[::-1]

def cntains_word(word, text):
	if is_palindrome(word):
		return text.count(word)
	return text.count(word) + text[::-1].count(word) 


def word_counter():
	word= input("enter word ")
	print(word)
	size=input("enter matrix size N M:")
	print (word,size)


	n= int(size.split(' ')[0])
	m= int(size.split(' ')[1])

	if len(word)>min([n,m]):
		return "Invalid"

	word_occurances=0
	matrix= []
	rows_inpu=0
	print("enter matrix:")
	while rows_inpu<n:
		row_input=input()


		row=row_input.strip().split(' ')
		if len(row)!=m:
			return 'Wrong input'
		matrix.append(row)
		rows_inpu=rows_inpu+1


	for row in matrix:
			# row.reverse()
		if cntains_word(word,row):
			word_occurances+=1
	for i in range(m):
		column=[]
		for row in matrix:
			column.append(row[i])
			if cntains_word(word,column):
				word_occurances+=1

	return word_occurances
print(word_counter())
