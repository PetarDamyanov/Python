phone_dict={0:" ",1:"Up",2:"a",22:"b",222:"c",
	3:"d",33:"e",333:"f",
	4:"g",44:"h",444:"i",
	5:"j",55:"k",555:"l",
	6:"m",66:"n",666:"o",
	7:"p",77:"q",777:"r",7777:"s",
	8:"t",88:"u",888:"v",
	9:"w",99:"x",999:"y",9999:"z"
	}
def numbers_to_message(pressed_sequence):
	str_list=[]
	s=""
	for x in pressed_sequence:
		s+=(str(x))
	str_list=s.split("-1")
	nl=[]
	list_helper=[]
	for word in str_list:
		for letter in range(0,len(word)-1):
			list_helper.append(word[letter])
			if word[letter]==word[letter+1]:
				list_helper.append(word[letter+1])
			else:
				nl.append(list_helper)
				list_helper=[]
			# print(word[letter])	
		
		
	print(nl)
numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
# "abc"
numbers_to_message([2, 2, 2, 2])
# "a"
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
# "Ivo e Panda"