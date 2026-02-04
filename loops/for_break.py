fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # similar to while break when condition is met

for i in range(10):
    if i == 5:
        print("Reached 5, stopping the loop!")
        break
    print(i)

numbers = [1, 3, 7, 8, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number is {num}")
        break

words = ["apple", "banana", "cherry", "date"]
for word in words:
    if word == "cherry":
        print("Found cherry! Exiting loop.")
        break
    print(word)

responses = ["no", "no", "yes", "no"]
for response in responses:
    if response == "yes":
        print("User agreed!")
        break
    print("Waiting for agreement...")
