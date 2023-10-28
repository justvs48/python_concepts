def armstrong(no):
    i=no 
    count=0
    j=no
    temp=0

    # 253
    while(i!=0):
        count+=1        
        i=i//10
    c=count
    while(c):
        rem=j%10
        temp+=(rem**count)
        j//=10
        c-=1
    if temp==no:
        print('armstrong')
    else :
        print('not armstrong')


    
no=int(input('enter the no: '))
armstrong(no)
