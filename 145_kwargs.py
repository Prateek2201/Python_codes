#   **keywword args
def func(**kwargs):
    #print(kwargs)
    #print(type(kwargs))
    for k,v in kwargs.items():
        print(f'{k}: {v}')
d={'name': 'prateek','age': 24}
func(**d)
#func(fname='harshit',lname='vashistha')
