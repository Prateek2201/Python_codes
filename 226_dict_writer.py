from csv import DictWriter
with open('DictWriter.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow, writerows
    csv_writer.writerow({
        'firstname' : 'harshit',
        'lastname' : 'vashisth',
        'age' : 24
        })
    csv_writer.writerow({
        'firstname' : 'prateek',
        'lastname' : 'agrahari',
        'age' : 19
        })

    csv_writer.writerows([
        {'firstname' : 'harshit','lastname' : 'vashisth','age' : 24},
        {'firstname' : 'prateek','lastname' : 'agrahari','age' : 19}
        ])
