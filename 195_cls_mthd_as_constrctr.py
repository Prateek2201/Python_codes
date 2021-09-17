class Person:
    cnt= 0      # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.cnt+=1
        self.fname= first_name
        self.lname= last_name
        self.age= age

    @classmethod
    def from_str(cls, s):
        fname, lname, age= s.split(',')
        return cls(fname,lname,age)
    
    @classmethod
    def count_inst(cls):
        return f'You have created {cls.cnt} instances of {cls.__name__} class '

    #instance methods
    def full_name(self):
        return f'{self.fname} {self.lname}'

    def is_above_18(self):
        return self.age>18

p1= Person('Prateek','Agrahari',19)
p2= Person('Harshit','Vashistha',24)

p3= Person.from_str('Harshit,Vashistha,24')
print(p3.full_name())

