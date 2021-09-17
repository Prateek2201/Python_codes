def divide(a,b):
    try:
        res= a/b
    except ZeroDivisionError as err:
##        print('please don\'t divide by zero ')
        print(err)
    except TypeError as err:
        print('please input numbers only')
##        print(err)
    except:
        print('unexpected error ...')
    else:
        return res
print(divide('4',2))
