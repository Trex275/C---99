#write a python script to move the contents of one folder inside th eanother. 
import os
import shutil

source = input("enter source folder path:- ")
destination = input("enter destination folder path")

source = source + '/'
destination = destination + '/'

list_of_file = os.listdir(source)

for file in list_of_file:
    shutil.move((source+file), destination)