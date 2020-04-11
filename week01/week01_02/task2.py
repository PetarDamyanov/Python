def is_number_balanced(number):
    if number>-9 and number<9:
    	return True	
    num=str(number)
    n1=[]
    n2=[]
    for x in range(0,len(num)):
    	if x<(len(num)-1)/2:
    		n1.append(int(num[x]))
    	elif x==(len(num)-1)/2:
    		pass
    	else:
    		n2.append(int(num[x]))		
    
    if sum(n1)==sum(n2):
    	return True
    else:
    	return False


    # print(n1)
    # print(n2)


print(is_number_balanced(9))

print(is_number_balanced(4518))

print(is_number_balanced(28471))

print(is_number_balanced(1238033))