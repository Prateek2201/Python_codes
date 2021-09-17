##fru=['grapes','mango','apple']
##fru.sort()
##print(fru)

##fru2=('grapes','mango','apple')
##print(sorted(fru2))
##print(fru2)

##fru3={'grapes','mango','apple'}
##print(sorted(fru3))
##print(fru3)

guitars= [
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith naptune', 'price':50000},
    {'model': 'faith apollo venus', 'price':35000},
    {'model': 'taylor 814ce', 'price':450000}
]

#s= sorted(guitars,key=lambda d: d.get('price'))
s= sorted(guitars,key=lambda d: d['price'],reverse=True)
print(s)
