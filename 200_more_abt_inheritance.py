# we can derive more than one class from base class?
# multilevel inheritance
# method resolution order
# isinstance(), issubclass()

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

    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, int_mem, rear_cam, frnt_cam):
        super().__init__(brand, model_name, price, ram, int_mem, rear_cam)
        self.frnt_cam= frnt_cam

    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price} and front_camera= {self.frnt_cam}'

#p= Phone('nokia', '1100', 1000)
sp= Smartphone('onePlus', '5', 3000, '6 GB', '64 GB', '20 MP')
fsp= FlagshipPhone('onePlus', '5t', 3000, '6 GB', '64 GB', '20 MP', '16MP')
#print(fsp.full_name())
#print(help(FlagshipPhone))
#print(isinstance(sp, FlagshipPhone))
#print(isinstance(fsp, Phone))
print(issubclass(FlagshipPhone, Smartphone))

