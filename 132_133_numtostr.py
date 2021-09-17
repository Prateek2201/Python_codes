def numtostr(li):
    return [str(i) for i in li if (type(i)==int or type(i)==float)]

li=[True,False,[1,2,3],1,1.0,3]
print(numtostr(li))
