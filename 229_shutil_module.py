import os
import shutil

os.chdir(r'E:\Python')
##print(os.listdir())

##fileiter = os.walk(r'E:\Python\movies')
##for cur_path,fold_name,file_name in fileiter:
##    print(f'cur_path: {cur_path}')
##    print(f'fold_name: {fold_name}')
##    print(f'file_name: {file_name}')

##os.rmdir('movies')
##os.makedirs('new/new1')

##shutil.rmtree('movies')
##shutil.copytree('new','copy\\new66')
##shutil.copy('new\\New Text Document.txt','copy\\new6')

##shutil.move('copy\\new6.txt','new//file1.txt')
shutil.move('copy','new//c')
