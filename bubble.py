a=[32,51,27,85,66,23]
i,n=0,5
while i<=n-1:
    ptr=0
    while ptr<=n-1-i:
        if a[ptr]>a[ptr+1]:
            a[ptr],a[ptr+1]=a[ptr+1],a[ptr]
        else:
            ptr=ptr+1
    i=i+1
print(a)
