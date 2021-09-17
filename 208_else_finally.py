# else and finally clause in exception handling

while True:
    try:
        number= int(input('enter a number: '))
    except ValueError:
        print('Please type integer !! ')
    except:
        print('inexcepted error !!! ')
    else:   # readability
        print(f'user input: {number}')
        break
    finally:    #resource release
        print('finally block .....')
        
