#import (os allows python to interact with files) (shutil  allows to make changes to files)
import os
import shutil

#user input to check for path
path = input("Please enter the file path: \n")

#check if exists and is a directory
if os.path.exists(path) and os.path.isdir(path):
    print("Path is valid. Continuing..")
else:
    print("invaid path or not a directory.")

#retrive list of items
items = os.listdir(path)

#create loop through each items
for item in items:
    full_path = os.path.join(path, item)

    #check is a file and not folder (os.path.splitext() always splits at the last period)
    if os.path.isfile(full_path):
        #get file extension
        name, extension = os.path.splitext(item)


#print(f ..) tells python to print a string that may contain a variable
print(f"Found file: {item} | Extension: {extension}")