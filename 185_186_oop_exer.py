class Laptop:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.name= brand + ' ' + model
        
l1= Laptop('hp','au114tx',63000)
l2= Laptop('dell','i3',33000)
print(l1.name)
print(l2.brand)
