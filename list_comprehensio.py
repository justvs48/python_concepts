language="python"
char=list(language)
print(char)


##########or OR 
lang2="english"
lanchar=[i for i in lang2]
print(type(lanchar))
print(lanchar)
##################

number=[i for i in range(0,11,2)] #0to10 with 2step
print(number) #[0, 2, 4, 6, 8, 10]


even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
#OUTPUT [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_numbers)  



