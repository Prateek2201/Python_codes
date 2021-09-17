class Laptop:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.name= brand + ' ' + model

    def apply_discount(self, n):
        return self.price - self.price*(n/100)
        
l1= Laptop('hp','au114tx',63000)
l2= Laptop('apple','macbook pro',230000)
print(l2.apply_discount(5))
