#PADK
#parameters >> *args >> default parameters >> **kwargs
def func(name,*args,lastname='unknown',**kwargs):
    print(name)
    print(args)
    print(lastname)
    print(kwargs)

func('harshit',1,2,3,a=1,b=2)
