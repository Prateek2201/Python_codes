nums=[3,4,2,1,5,6,9,8,10]
#print(list(map(lambda a:a%2==0, num)))
print(list(filter(lambda a:a%2==0, nums)))

evens= [i for i in nums if i%2==0]
print(evens)
