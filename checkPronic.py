import math as m
inpstr=input()
s=set()
outarr=[]
for i in range(0,len(inpstr)):
    for j in range(i,len(inpstr)):
        s.add(int(inpstr[i:j+1]))
temp = sorted(list(s))
##print(temp)
for i in temp:
    for j in range(1,int(m.sqrt(i))+1):
        if j*(j+1)==i:
            outarr.append(i)
            break
if(len(outarr)==0):
    outarr.append(-1)
print(outarr)
