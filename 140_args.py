# make flexible functions
# *operator
# *args

def all_total(*args):
    total=0
    for i in args:
        total+=i
    return total
print(all_total(1,2,3,4))
