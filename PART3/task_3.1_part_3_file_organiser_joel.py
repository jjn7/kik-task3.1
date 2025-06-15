#import (os allows python to interact with files) (shutil  allows to make changes to files)
import os
import shutil

#user input to check for path
path = input("Please enter the file path: ")
if os.path.exists(path) and os.path.isdir(path):
    print("Path is valid. Continuing..")
else:
    print("invaid path or not a directory.")
