import os
import shutil

source = input("Enter source folder namer : ")
destination = input("Enter destination folder name : ")
source = source+"/"
desination = destination+"/"
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.move((source+file),destination)