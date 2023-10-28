# ############################################
#this will get unique char

name1=input("enter your name :  ")
name2=input("enter other name : ")
nam1list = list(name1)
print(nam1list)
nam2list = list(name2)
print(nam2list)
common_char=[]
m=0
for i in range(len(nam1list)):
    print(i)
    for j in range(len(nam2list)):
        if nam1list[i]==nam2list[j]:
            # common_char.append(nam1list[i])
            nam1list[i]=m
            nam2list[j]=m
            m+=1
            break

newlist=nam1list+nam2list
for i in range(m):
    newlist.remove(i)
    newlist.remove(i)
print(newlist)
########################################

## flames=list('flames')
## cout=7
##for i in 

