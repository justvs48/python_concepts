def fib(key):
    lis=[0,1]
    while(lis[-1]<key):
        lis.append(lis[-1]+lis[-2])
    return lis[:-1]
key=int(input('enter the Key: '))
lis=fib(key)
for i in lis:
    print(i)