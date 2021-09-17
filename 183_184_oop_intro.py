# init() method-- constructor

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method / constructor get called')
        self.fname= first_name
        self.lname= last_name
        self.age= age

p1= Person('Prateek','Agrahari',19)
p2= Person('Harshit','Vashistha',24)
print(p1.fname)   
print(p2.fname)   
