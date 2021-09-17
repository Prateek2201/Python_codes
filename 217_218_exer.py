with open('salary.txt','r') as rf:
    with open('new_salary.txt','a') as wf:
        for line in rf.readlines():
            name, sal= line.split(',')
            wf.write(f'{name}\'s salary is {sal}')
        
