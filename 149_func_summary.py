def add(a,b):
    return a+b

def dynamic_add(*args):
    t=0
    for i in args:
        t+=i
    return t

print(dynamic_add(1,2,3,4))

l=[1,2,3,4]
print(dynamic_add(*l))

#kwargs-keyword argument, **
def func(**kwargs):
    print(kwargs)   #gathers as dict

func(name='Prateek',age='19')


#PADS
def func2(name,*args,lastname='Agrahari',**kwargs):
    print(name)
    print(args)
    print(lastname)
    print(kwargs)

func2('Prateek',1,2,3,age=19)
