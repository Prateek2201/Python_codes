class Laptop:
    dis= 10
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.name= brand + ' ' + model

    def apply_discount(self):
        return self.price - self.price*(self.dis/100)
        
#Laptop.dis= 100
l1= Laptop('hp','au114tx',63000)
l2= Laptop('apple','macbook pro',230000)
l2.dis= 50
print(l2.apply_discount())
print(l2.__dict__)
