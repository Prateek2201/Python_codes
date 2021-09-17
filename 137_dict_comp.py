#dictionary compression
#square={1: 1, 2: 4, 3: 9}
sq={num:num**2 for num in range(1,11)}
print(sq)
##sq1={f'Square of {num} is: ':num**2 for num in range(1,11)}
##print(sq1)
##for num in range(1,11):
##    print(f'Square of {num} is: {num**2}')
for k,v in sq.items():
    print(f'{k}: {v}')


#char-conuter
s='harshit'
counter={char:s.count(char) for char in s}
print(counter)
