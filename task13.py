def max_consecutive(items):
    c=1
    cmax=0
    i=0
    j=1
    while j<len(items):
    	if items[i]==items[j]:
    		c=c+1
    	if items[i]!=items[j]:
    		if cmax<c:
    		  cmax=c
    		c=0
        i=i+1
    	j=j+1
    print(c)
max_consecutive([1, 2, 3, 3, 3, 3, 4, 3])

max_consecutive([1, 1, 2, 3, 3, 4,4, 5, 5])

max_consecutive([1,2,3,3,3,3,4,5])