#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
f = open("demofile.txt", "rt") #r for read; t for text

print(f.read())  # to print the file
#if file in different location
f = open("D:\\myfiles\welcome.txt")

with open("demofile.txt") as f:
  print(f.read()) 
  
f = open("demofile.txt")
print(f.readline()) # returns only one line


with open("demofile.txt") as f:
  print(f.read(5)) #can specify how many characters to return

with open("demofile.txt") as f:#loops through the file line by line
  for x in f:
    print(x) 

f.close()  #close when done
