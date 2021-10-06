#Write  a python script that takes the path of a folder that needs to 
#be organised. 

import os
import shutil

path = input("enter the path of directory you wish to organize :-")
list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)
    #stores the extension type
    ext = ext[1:]
    #this forces the next iteration if its a folder
    if ext == '':
        continue
    
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
