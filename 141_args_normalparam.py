#def mult(num,*args):
def mult(*args):
    tot=1
    print(args)
    for i in args:
        tot*=i
    return tot
print(mult(3,4))
