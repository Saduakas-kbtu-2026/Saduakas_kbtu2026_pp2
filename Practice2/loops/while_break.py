i = 1
while i < 6:
  print(i)
  if i == 3:
    break # stops loops when condition is met
  i += 1 

count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        print("Reached 5, stopping the loop!")
        break

user_inputs = ["no", "maybe", "yes", "no"]
index = 0

while index < len(user_inputs):
    if user_inputs[index] == "yes":
        print("User agreed!")
        break
    print("Waiting for agreement...")
    index += 1

num = 10
while True:
    if num % 7 == 0:
        print(f"{num} is divisible by 7, stopping the loop!")
        break
    num += 1

n = 10
while n > 0:
    print(n)
    n -= 1
    if n == 3:
        print("Stopping countdown at 3")
        break
