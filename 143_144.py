def to_power(num,*args):    #tuple passed
    if args:    #len(args)>0:
        return [i**num for i in args]
    else:
        return 'Hey you didn\'t pass any args'
nums=[1,2,3]
print(to_power(3,*nums))
