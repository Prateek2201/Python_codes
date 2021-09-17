# create first generator with generator func
# 1. generator func 2. generator comrehension
def nums(n):
    for i in range(1,n+1):
        yield(i)    #yield i

number = nums(10)
for num in number:
    print(num)

for num in number:
    print(num)
