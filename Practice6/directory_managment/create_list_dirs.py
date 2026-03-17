import os
path = "project/data/raw"
# create nested directories
os.makedirs(path, exist_ok=True)

import os
folder = "project"
#list files and folders
items = os.listdir(folder)
for item in items:
    print(item)


import os
folder = "project"
for item in os.listdir(folder): #seperating files and directories
    path = os.path.join(folder, item)

    if os.path.isfile(path):
        print("File:", item)
    elif os.path.isdir(path):
        print("Folder:", item)

#using pathlib seperating files and directories
from pathlib import Path
folder = Path("project")
for item in folder.iterdir():
    print(item)


import os
folder = "project"#find files using extensions
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))


from pathlib import Path
folder = Path("project")#find files using pathlib
for file in folder.rglob("*.txt"):
    print(file)
