with open('file.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        wf.write(rf.read())
