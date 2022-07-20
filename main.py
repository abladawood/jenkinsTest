import os
for path, subdirs, files in os.walk(params.folderPath):
    for name in files:
        print(os.path.join(path, name))


