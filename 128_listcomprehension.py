#create a list of squares from 1 to 10
square=list(i**2 for i in range(1,11))
print(square)

neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)

negative=list(-i for i in range(1,11))
print(negative)

#print first char of string of list
s1=[]
s=['Rohit','Mohit','Adi']
for i in s:
    s1.append(i[0])
print(s1)

s1=list(names[0] for names in s)
print(s1)
