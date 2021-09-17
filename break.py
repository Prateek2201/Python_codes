av=5
x= int(input("How many candies you want?"))
for i in range(1,x):
    if i>av:
        print("Out of stock")
        break
    print("Candy ")
print("Bye")