import os
import sys
print(sys.argv[1])
filePath = sys.argv[1]
for path,subdir,files in os.walk(filePath):
    for file in files:
        for subfile in file:
            print(os.path.join(subfile,file,path))

