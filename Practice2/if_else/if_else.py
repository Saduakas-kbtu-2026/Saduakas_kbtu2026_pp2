a = 200
b = 33
if b > a:
  print("b is greater than a")
else: # falls back  on else if main if argument is failed
  print("b is not greater than a") # prints this statement in this case

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd") # prints this statement

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
