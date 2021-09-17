largest = None
smallest = None
lst=[]
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break    
    try:
      	n = int(num)
    except:
    	print('Invalid input')
    else:
        lst.append(n)

lst.sort()
largest = lst[-1]
smallest = lst[0]
print("Maximum is", largest)
print("Minimum is", smallest)
