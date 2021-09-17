
names=['abc','def','ghi']
##for i in range(len(names)):
##    print(f'{i} -- {names[i]}')

##pos=0
##for name in names:
##    print(f'{pos} ---> {name}')
##    pos+=1

#with enumerate function
##for pos,name in enumerate(names):
##    print(f'{pos} ---> {name}')

#finding pos
def find_pos(names,target):
    for pos,name in enumerate(names):
        if name == target:
            return pos        
    return -1
print(find_pos(names,'def'))
            
