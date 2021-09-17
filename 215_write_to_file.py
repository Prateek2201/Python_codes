# w a r+

#with open('file.txt', 'w') as f:
#with open('file.txt', 'a') as f:
with open('file2.txt', 'r+') as f:
    f.seek(len(f.read()))
    data= f.write('plz do it')
    f.seek(0)
    print(f.read())
