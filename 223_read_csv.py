from csv import reader
with open('file.csv', 'r') as f:
    csv_reader = reader(f)  # iterator
    #print(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        print(row)
    
