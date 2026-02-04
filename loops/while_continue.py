i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #stop the current iteration, and continue with the next:
  print(i)

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

numbers = [3, -1, 5, -2, 7]
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        index += 1
        continue  # Skip negative numbers
    print(numbers[index])
    index += 1

num = 1
while num <= 10:
    if num % 3 == 0:
        num += 1
        continue  # Skip multiples of 3
    print(num)
    num += 1

n = 0
while n < 10:
    n += 1
    if n < 5:
        continue  # Skip numbers less than 5
    print(n)
