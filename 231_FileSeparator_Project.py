import os,shutil

dict_ext = {
    'aud_ext' : ('mp3','mpa','wav','flac'),
    'vid_ext' : ('mp4','mkv','MKV','flv','mpeg'),
    'doc_ext' : ('doc','docx','pdf','txt'),
    'img_ext' : ('jpg','jpeg')
}

folder_path = input('Enter folder path : ')

def file_finder(path, extns):
##    files = []
##    for file in os.listdir(path):
##        for ext in extns:
##            if file.endswith(ext):
##                files.append(file)
##    return files
    return [file for file in os.listdir(path) for ext in extns if file.endswith(ext)]
    
#print(file_finder(folder_path,vid_ext))
for ext_type,ext_tup in dict_ext.items():
##    print(f'calling file finder-- {ext_type}')
##    print(file_finder(folder_path,ext_tup))
    folder_name = ext_type.split('_')[0]+' Files'
    folder_new_path = os.path.join(folder_path, folder_name)
    os.mkdir(folder_new_path)
    for item in file_finder(folder_path,ext_tup):
        item_path = os.path.join(folder_path, item)
        item_new_path = os.path.join(folder_new_path, item)
        shutil.move(item_path, item_new_path)
