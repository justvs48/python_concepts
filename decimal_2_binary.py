x=47
binarys=[]
i=0
while x!=0:
    rem=x%2
    binarys.append(rem)
    # binarys[i]=rem this is wrong as it we have not specified any length in binarys list
    
    x=x//2
    i+=1
binarys.reverse()
print(binarys)

