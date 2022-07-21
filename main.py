import os
import sys
print(sys.argv)
filePath = '/Users/ablosh/Desktop/Semester B'
for path,subdir,files in os.walk(filePath):
    for file in files:
        for subfile in file:
            print(os.path.join(subfile,file,path))

