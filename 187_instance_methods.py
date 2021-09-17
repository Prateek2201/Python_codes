# init() method-- constructor

class Person:
    def __init__(self, first_name, last_name, age):
        self.fname= first_name
        self.lname= last_name
        self.age= age

    #instance methods
    def full_name(self):
        return f'{self.fname} {self.lname}'

    def is_above_18(self):
        return self.age>18

p1= Person('Prateek','Agrahari',19)
p2= Person('Harshit','Vashistha',24)
print(p1.full_name())
print(Person.full_name(p2))
print(p1.is_above_18())


l= [1,2,3]
##l.clear()
##print(l)
##list.clear(l)
##print(l)
list.append(l,5)
print(l)
