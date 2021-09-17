# Name mangling--- __name (not a convention)

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand= brand
        self._model_name= model_name
        self.__price= price

    def make_a_call(self, ph_no):
        print(f'calling {ph_no} ...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_msg():
        pass    # twilio

p1= Phone('Nokia','1100',1000)
#print(p1._price)
print(p1._Phone__price)
print(p1.__dict__)

##p1._price= -1000
##print(p1._price)

# _name--- convention for private name
# __name__--- dunder/magic methods 
##l= [3,2,1,4]
##l.sort()    # tim sort
##print(l)
