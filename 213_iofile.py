# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

f= open('file1.txt')
##print(f'cursor position - {f.tell()}')
##print(f.read())
##print(f'cursor position - {f.tell()}')
##print('before seek method')
##f.seek(0)
##print('after seek method')
##print(f'cursor position - {f.tell()}')
##print(f.read())

##print(f.readline(), end='')
##print(f.readline(), end='')
##print(f.readline(), end='')

##lines= f.readlines()
##print(len(lines))
for line in f.readlines()[:2]:
    print(line, end='')

# name, closed--- data discriptor

##f= open(r'C:\Users\computer\Desktop\file1.txt')
##print(f.name)
##print(f.closed)
f.close()
print(f.closed)
