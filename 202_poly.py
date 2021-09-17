# special magic methods / dunder methods
# operator overloading
# polymorphism--- method overriding

class Phone:    # base class / parent class
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= max(price,0)

    def phone_name(self):
        return f'{self.brand} {self.model}'

    def __str__(self):  # nicely-formatted string
        return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self): # code
        return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price})'

    def __len__(self):
        return len(self.phone_name())

    def __mul__(self, other):
        return self.price * other.price

class Smartphone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __len__(self):
        return self.price
        
##l=[1,2,3]
##print(len(l))
##t=[1,2,3]
##print(len(t))
##s= 'Harshit'
##print(len(s))

p= Phone('nokia', '1100', 1000)
p2= Phone('nokia', '1600', 1200)
sp= Smartphone('oneplus', '5t', 33000, '16 MP')
print(sp.phone_name())
print(p.phone_name())
print(len(p))
print(len(sp))

##print(p * p2)

##print(len(p))
##print(str(p))
##print(repr(p))
##print(p.__repr__())

