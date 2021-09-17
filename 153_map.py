##numbers=[1,2,3,4]
##def sq(a):
##    return a**2
##
###squares= list(map(sq,numbers))
##squares= list(map(lambda a:a**2,numbers))
##print(squares)
##
###list comp
##square= list(a**2 for a in numbers)
##print(square)
##
##square2=[]
##for a in numbers:
##    square2.append(sq(a))
##print(square2)


names=['abc','abcd','abcde']
length=list(map(len, names))
print(length)
