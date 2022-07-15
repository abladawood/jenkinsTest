import os
for path, subdirs, files in os.walk(/Users/ablosh/Desktop/Semester B):
    for name in files:
        print(os.path.join(path, name))


