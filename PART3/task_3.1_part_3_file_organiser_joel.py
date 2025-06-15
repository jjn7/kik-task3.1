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

#Create a dictionary of file types for sorting
categories = {
    "Documents": [".pdf", ".doc", ".docx", ".docm", ".txt", ".rtf", ".csv", ".xlsx", ".xls", ".xps", ".xml", ".odt", ".ott", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".bmp", ".png", ".gif", ".exif", ".ico", ".heif", ".heic", ".ttif", ".tif", ".webp"],
    "Videos": [".3pg", ".avi", ".mpeg", ".m4v", ".mov", ".webm", ".ogg"],
    "Music": [".mp3", ".mp4", ".wav", ".avif", ".raw", ".flac", ".wma", ".ac3", ".aac", ".midi"],
    "Archives": [".zip", ".rar", ".7z", ".arc", ".cab", ".tar"]
}

#check files in directory and subfolders
for root, dirs, files in os.walk(path):
    for item in files:
        full_path = os.path.join(root, item)

        #check is a file and not folder (os.path.splitext() always splits at the last period)
        if os.path.isfile(full_path):
            #get file extension
            name, extension = os.path.splitext(item)

            #create check for which category the file type belongs to
            for category, extensions in categories.items():
                if extension.lower() in extensions:
                    target_folder = os.path.join(path, category)
                    #grant permossion for os to create directories
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder,)
                    break
            else:
                target_folder = os.path.join(path, "Other")
                if not os.path.exists(target_folder):
                        os.makedirs(target_folder,)

            #move the files into new directory    
            shutil.move(full_path, os.path.join(target_folder, item))
            print(f"Moved: {item} to {target_folder}")