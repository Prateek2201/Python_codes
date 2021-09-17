from csv import DictReader,DictWriter
with open('DictWriter.csv', 'r') as rf:
    with open('Dict.csv', 'w', newline='') as wf:
        re = DictReader(rf)
        wr = DictWriter(wf,fieldnames=['first_name','last_name','age'])
        wr.writeheader()
        for row in re:
            fname,lname,age = row['firstname'],row['lastname'],row['age']
            wr.writerow({
                'first_name': fname.upper(),
                'last_name': lname.upper(),
                'age': age
                })
        
