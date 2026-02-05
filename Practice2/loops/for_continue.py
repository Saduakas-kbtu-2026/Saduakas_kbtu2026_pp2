fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue#also like while loop, stop this current iteration and continue at the next
  print(x)

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

words = ["apple", "banana", "cherry", "date"]
for word in words:
    if word == "banana":
        continue  # Skip banana
    print(word)

for num in range(1, 11):
    if num % 3 == 0:
        continue  # Skip multiples of 3
    print(num)

numbers = [4, -1, 7, -3, 0, 5]
for n in numbers:
    if n < 0:
        continue  # Skip negative numbers
    print(n)
