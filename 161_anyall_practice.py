def sum(*args):
    if all((type(arg)==int or type(arg)==float for arg in args)):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return 'Wrong input'
print(sum(1,2,3,4,12.5))
