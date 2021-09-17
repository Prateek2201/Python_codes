class Person:
    cnt= 0
    def __init__(self):
        Person.cnt+=1

p1= Person()
p2= Person()
p3= Person()
print(Person.cnt)

