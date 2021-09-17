##def func(item):
##    return len(item)

names=['prateek','harshit','ab']
print(max(names,key=lambda item:len(item)))

s=[
    {'name':'prateek','score':90,'age':19},
    {'name':'harshit','score':89,'age':24},
    {'name':'harsh','score':79,'age':23}
]
print(max(s,key=lambda item:item.get('score')).get('name'))
print(max(s,key=lambda item:item.get('age'))['name'])

s1={
    'prateek': {'score':90,'age':19},
    'harshit': {'score':89,'age':24},
    'harsh': {'score':79,'age':23}
}
print(max(s1,key= lambda item:s1[item]['score']))
