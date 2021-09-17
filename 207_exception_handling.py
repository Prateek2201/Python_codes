# try except else finally

while True:
    try:
        age= int(input('enter your age: ')) # seven
        break
    except ValueError:
        print('may be you enntered string instead of number, try again')
    except:
        print('unexcepted error...')


if age < 18:
    print('You can\'t play this game. ')
else:
    print('You can play this game. ')
