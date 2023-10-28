def fibonaci(lims):
    a=0
    b=1
    temp=0
    fiblist=[a,b]
    while(temp<=lims):
        temp=a+b
        if temp>lims:
            break
        else:
            
            a=b
            b=temp
            fiblist.append(temp)
        
    return fiblist

lim=int(input('enter the limit: '))
print(fibonaci(lim))





