with open('emojy.txt', 'r', encoding='utf-8') as f:
    print(f.encoding)
    data= f.read(10)
    while len(data)>0:
        print(data)
        data= f.read(10)
