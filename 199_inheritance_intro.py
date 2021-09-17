class Phone:    # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand= brand
        self.model_name= model_name
        self._price= max(price,0)

    def full_name(self):
        return f'{self.brand} {self.model_name}'
    
    def make_a_call(self, ph_no):
        print(f'calling {ph_no} ...')

class Smartphone(Phone):    # derived / child class
    def __init__(self, brand, model_name, price, ram, int_mem, rear_cam):
        #Phone.__init__(self, brand, model_name, price) # uncommon way
        super().__init__(brand, model_name, price)
        self.ram= ram
        self.int_mem= int_mem
        self.rear_cam= rear_cam

p= Phone('nokia', '1100', 1000)
sp= Smartphone('onePlus', '5', 3000, '6 GB', '64 GB', '20 MP')
print(p.full_name())
print(sp.full_name() + f' and price is {sp._price}')
