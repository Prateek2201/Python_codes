l=[1,2,3,4]
def s(a):
    return a**2

sq=list(map(s, l))
print(sq)
#sq=list(map(lambda i:i**2, l))

def my_map(func, l):
    new=[]
    for i in l:
        new.append(func(i))
    return new

def my_map1(func, l):
    return [func(i) for i in l]

print(my_map1(lambda i:i**3,l))
