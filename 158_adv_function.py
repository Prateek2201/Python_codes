l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
def avg_finder(*args):      #taking tuple of lists
    avg=[]
    for pair in zip(*args): #unpacking
        avg.append(sum(pair)/len(pair))
    return avg

print(avg_finder(l1,l2,l3))

avg_finder= lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
#print(av(l1,l2,l3))
