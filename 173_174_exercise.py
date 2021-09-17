from functools import wraps
import time
##t1= time.time()
##print('this is line 1')
##x=5
##if x==5:
##    print('x==5')
##print('this is line 2')
##t2= time.time()
##print(t2-t1)

def calc_time(f):
    @wraps(f)
    def wrapper_func(*args,**kwargs):
        print(f'executing ... {f.__name__}')
        t1=time.time()
        ret= f(*args,**kwargs)
        t2=time.time()
        tot= t2-t1
        print(f'this functin took {tot} seconds')
        return ret
    return wrapper_func

@calc_time
def sq_finder(n):
    return [i**2 for i in range(1,n+1)] 

print(sq_finder(10))
