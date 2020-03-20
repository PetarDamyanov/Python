def increasing_or_decreasing(seq):
    i=0
    j=1
    flag=0
    while j<len(seq):
    	# print(seq[j])
    	# print(seq[i])
    	if (seq[j]-seq[i])==1:
    		flag="UP"
    	elif (seq[i]-seq[j])==1:
    		flag="DOWN"
    	else:
    		return False	
    	i+=1
    	j+=1
    return flag

print(increasing_or_decreasing([1,2,3,4,5]))

print(increasing_or_decreasing([5,6,-10]))

print(increasing_or_decreasing([1,1,1,1]))

print(increasing_or_decreasing([9,8,7,6]))
