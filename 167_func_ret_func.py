def outer_func():
    def inner_func():
        print('Inside inner function')
    return inner_func()
var= outer_func()
#var()


def outer(msg):
    def inner():
        print(f'Message is {msg}')
    return inner
var=outer('Hi there !')
var()
