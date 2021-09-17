##def is_even(a):
##    return a%2==0
##print(is_even(5))
##
##is_even2=lambda a:a%2==0
##print(is_even2(6))

##def last_char(s):
##    return s[-1]
##print(last_char('Prateek'))
##
##last_char2=lambda s: s[-1]
##print(last_char2('Prateek'))

def f(s):
    if len(s)>5:
        return True
    return False
print(f('Prateek'))

func=lambda s:True if len(s)>5 else False
print(func('Prateek'))

func2=lambda s: len(s)>5
print(func2('harsh'))
