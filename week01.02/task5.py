def sum_of_numbers(input_string):
	if input_string.isdigit():
		return int(input_string)
	sum_of_digits=0
	i=0
	for x in input_string:
		if x.isdigit():
			pass
		else:
			input_string=input_string.replace(x," ")		

	# print(input_string)

	for x in input_string.strip(' ').split(' '):
		if x.isdigit():
			sum_of_digits+=int(x)
	print(sum_of_digits)

sum_of_numbers("ab125cd3")

sum_of_numbers("ab12")

sum_of_numbers("ab")

print(sum_of_numbers("1101"))

sum_of_numbers("1111O")

sum_of_numbers("1abc33xyz22")

sum_of_numbers("0hfabnek")