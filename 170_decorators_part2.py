def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print('this is awesome function')
        return any_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def func(a):
    print(f'this is function with argument {a}')

func(7)

@decorator_func
def add(a,b):
    return a+b

print(add(2,3))
