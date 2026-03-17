#before modifying a file we must open the file beforehand
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())  #will keep adding lines to file

#will overwrite entire file
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 

#creates new file myfile
f = open("myfile.txt", "x")
