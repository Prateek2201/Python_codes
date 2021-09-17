import os
##print(os.getcwd())
##os.mkdir('movies')
##print(os.path.exists(os.getcwd()))
##print(os.path.exists('movies'))
##if os.path.exists('movies'):
##    print('already exists')
##else:
##    os.mkdir('movies')

##open(r'movies\file.txt','a').close()
##os.chdir(r'E:\Python\movies')
##print(os.listdir(r'E:\Python\movies'))
for list in os.listdir(r'E:\Python\movies'):
    #print(os.getcwd()+'\\'+list)
    print(os.path.join(os.getcwd(),'movies',list))
    
