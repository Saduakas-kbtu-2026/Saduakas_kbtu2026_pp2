import os
os.remove("demofile.txt") #removes the demo file from computer

import os
if os.path.exists("demofile.txt"): #prelimary check for existance of file
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

import os
os.rmdir("myfolder") #to delete entire folder !rmdir!

with open("newtext.txt", "w") as f: #scuffed copy method
  l = open("test_text.txt", "rt")
  l_text = l.read()
  f.write(l_text)
