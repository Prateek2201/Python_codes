# Decorators-- enhance the functionality of other functions
# @-- use for decorator called as 'syntatic sugar'

def decorator_func(any_func):
    def wrapper_func():
        print('this is awesome function')
        any_func()
    return wrapper_func

@decorator_func     # shortcut
def func1():
    print('this is func1')

@decorator_func 
def func2():
    print('this is func2')

##func1()
##func2()

#func1= decorator_func(func1)
func1()
func2()
