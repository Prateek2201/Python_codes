t=int(input())
res=[]
for i in range(t):
    n=int(input())
    li=list(map(int,input().split(' ')[:n]))
    for i in range(n):
        left,right=0,0
        for j in range(n):
            if j<i:
                left+=li[j]
            elif j>i:
                right+=li[j]
            else:
                left,right=left,right
        if left==right:
            t='Yes'
            res.append(t)
            break
    if left!=right:
        t='No'
        res.append(t)
for i in res:
    print(i)
        
        
    
