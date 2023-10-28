# for i in range(5):
#     for j in range(i+1):
#         print(i)


# def pascaltri(n):
#     tri=[]
#     for i in range(n):
#         row=[]
#         for j in range(i+1):
#             if (j==0 or j==i):
#                 row.append(1)
#             else:
#                 value=tri[i-1][j-1]+tri[i-1][j]
#                 row.append(value)
#         tri.append(row)
#     return tri
# n=5
# pascal=pascaltri(n)
# for i in pascal:
#     for j in i:
#         print(j)
#     print('\n')

def pascaltri(n):
    tri=[]
    value=0
    for i in range(n):
        row=[]
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)

            else:
                value=tri[i-1][j-1]+tri[i-1][j]
                
                row.append(value)
        tri.append(row)
    
    return tri




n=5
# print(pascaltri(n))

for i in pascaltri(n):
    for j in i:
        print(j,end=' ')
        
    print(end='\n=')

