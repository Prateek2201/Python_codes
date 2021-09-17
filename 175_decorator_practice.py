from functools import wraps

def only_int(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
##        data_types=[]
##        for arg in args:
##            data_types.append(type(arg)==int)
##        if all(data_types):
##            return func(*args,**kwargs)
##        else:
##            return 'Only int values allowed !'
        if all([type(arg)==int for arg in args]):
            return func(*args,**kwargs)
        else:
            return 'Only int values allowed !'
    return wrapper


@only_int
def add_all(*args):
    t=0
    for i in args:
        t+=i
    return t
print(add_all(1,2,3,4,1.3))
        
