import os
for path, subdirs, files in os.walk(env.folderPath):
    for name in files:
        print(os.path.join(path, name))


