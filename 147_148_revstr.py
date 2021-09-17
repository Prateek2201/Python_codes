names=['harshit','mohit']

def func(names,**kwargs):
    if kwargs.get('reverse_str'):
        return [name[::-1].title() for name in names]
    else:
        return [name.title() for name in names]

print(func(names,reverse_str=True))
