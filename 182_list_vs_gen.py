import time
#t1=time.time()
#l= [i**2 for i in range(10000000)]
#print(time.time()-t1)
#print(t2-t1)
t1=time.time()
g= (i**2 for i in range(10000000))
print(time.time()-t1)
