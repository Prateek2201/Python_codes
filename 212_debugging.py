import pdb

 # l n q c
name= input('plz type your name: ')
age= int(input('plz type you age: '))
print(f'hello {name} your age is {age}')
pdb.set_trace()
age2 = age + 5
print(f'{name} you will be {age2} in next five years')
