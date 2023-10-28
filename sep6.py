###########################################

# List

# mylist=["hlo", 'hi' ,"hru"]
# popelem=mylist.pop(1)
# print('popped element = ' , popelem)
# print (mylist)
# l1=['yo ' , 'hru', 'what are you']
# l1.remove("hru")
# new =mylist+l1
# print(new)
# new.insert(1,7)# no prob

# print(new[0])
# print(new)

# nestedlist=[1,2,new,3]
# print(nestedlist[2][0])
# print(new[0:2])

####################################################

# Sets

myset={1,2,3,3}
print (myset)
myset.add(4)
myset.remove(1)
print(myset)
smyset={2,5,6,7}
if 3 in myset:
    print('3 is present')
print('intersection: ',myset&smyset)
print("union : ",myset|smyset)
print("subtraction : ",myset-smyset)
