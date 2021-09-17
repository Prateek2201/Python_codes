from csv import writer
with open('csvwriter.txt','w', newline='') as f:
    csv_writer = writer(f)
    # methods to write--- writerow, writerows
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['mohit','INDIA'])
    csv_writer.writerow(['harshit','INDIA'])

    #csv_writer.writerows([['name','country'],['mohit','INDIA'],['harshit','INDIA']])
