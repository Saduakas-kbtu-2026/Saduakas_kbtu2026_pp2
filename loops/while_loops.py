i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break # stops loops when condition is met
  i += 1 


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #stop the current iteration, and continue with the next:
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else: # if initial condition is not met
  print("i is no longer less than 6")