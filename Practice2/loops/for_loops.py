fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # similar to while break when condition is met

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue#also like while loop, stop this current iteration and continue at the next
  print(x)

for x in range(6): #prints x 6 times
  print(x)

for x in range(2, 6):# x x x x
  print(x)

for x in range(2, 30, 3):# from 2 to 30, with increments of 3
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!") # prints a message when loop is finished

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #nested loop

for x in [0, 1, 2]:
  pass # basically ignores the loop; because loops cannot be empty
