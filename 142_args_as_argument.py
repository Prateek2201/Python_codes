def mult(*args):
    t=1
    for i in args:
        t*=i
    return t
nums=[2,3,4]    #(2,3,4)
print(mult(*nums))  #list unpacking
