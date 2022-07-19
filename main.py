import os
for path, subdirs, files in os.walk(${folderPath}):
    for name in files:
        print(os.path.join(path, name))


