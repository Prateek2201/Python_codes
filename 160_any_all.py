n1=[2,4,6,8,10]
n2=[1,2,3,4,5,6]

##evens1=[]
##for num in n1:
##    evens1.append(num%2==0)
##print(evens1)

print(all([num%2==0 for num in n1]))
print(any([num%2==0 for num in n2]))
