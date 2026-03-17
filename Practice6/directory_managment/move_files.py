#move files between directories
import shutil

source = "folder1/file.txt"
destination = "folder2/file.txt"

shutil.move(source, destination)

print("File moved successfully")

#move all files between directories 
import os
import shutil

source_folder = "folder1"
destination_folder = "folder2"

for file in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)

    shutil.move(source_path, destination_path)

#copy files between directories
import shutil

source = "folder1/file.txt"
destination = "folder2/file.txt"

shutil.copy(source, destination)

print("File copied successfully")

#copy files with certain extensions using pahtlib
from pathlib import Path
import shutil

src = Path("folder1/file.txt")
dst = Path("folder2/file.txt")

shutil.copy(src, dst)

#copy entire directories
import shutil

shutil.copytree("folder1", "folder_backup")
