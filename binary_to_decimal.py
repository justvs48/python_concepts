def bin_to_deci():
    binaryno=input("enter the binary no : ")
    mylist=[i for i in binaryno]
    length=len(mylist)


    bnarylist=[0]*length
    j=0
    for i in binaryno:
        bnarylist[j]=int(i)
        j+=1

    bnary=0
    length=len(bnarylist)

    for j in range(length):
        # print((length-1)-j)
        bnary+=(2**j)*bnarylist[(length-1)-j]
    print("binary to decimal : ",bnary)

def dec_to_bin():
    x=int(input("enter the no you want to convert :\n"))
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


def main():
    print("what do you want to do :")
    choice=int(input('Press 1 for dec to binary\nPress 2 for binary to decimal\nPress 0 for exit\n'))
    if choice==0:
        print('thankYou !!')
    elif choice==1:
        dec_to_bin()
        main()
    elif choice==2:
        bin_to_deci()
        main()
    else :
        print("wrong input") 
        main()       

main()
