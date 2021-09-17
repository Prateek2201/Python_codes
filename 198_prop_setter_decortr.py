# getter()--- @property
# setter()--- @getter_func_name.setter

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand= brand
        self.model_name= model_name
        self._price= max(price,0)
        #self.spec= f'{self.brand} {self.model_name} and price is {self._price}'

    @property
    def spec(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price= max(new_price, 0)
    
    def make_a_call(self, ph_no):
        print(f'calling {ph_no} ...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

p1= Phone('Nokia','1100',1000)
p1.price= -500
print(p1.price)
print(p1.spec)
