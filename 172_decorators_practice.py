from functools import wraps
def print_func_data(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        print(f'You are calling {any_func.__name__} function')
        print(f'{any_func.__doc__}')
        return any_func(*args, **kwargs)
    return wrapper_func
        

@print_func_data
def add(a,b):
    '''This function takes two arguments and return their sum '''
    return a+b

print(add(4,5))
#print(add.__doc__)
