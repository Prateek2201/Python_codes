num = int(input())
a= [1,2,5,6,6,5]
freq=list()
set_unique = set(a)

for i in set_unique:
    freq.append(a.count(i))

freq = sorted(freq)
ans = len(set_unique)
for cnt in freq:
    if cnt<=num:
        num = num-cnt
        ans = ans-1
    else:
        break
print(ans)
