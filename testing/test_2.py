# Comvert images into PDF

import os, fitz, pathlib

doc = fitz.open()
dirList = os.listdir(pathlib.Path(__file__).parent.resolve()) # locate program directory
imgList = []
for items in dirList:
    if os.path.splitext(items)[1] == ".jpeg": # verify file is .jpeg format
        imgList.append(items)
    
        
print(imgList)

