fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit) # start = 1, start count with 1 instead
#0 apple
#1 banana
#2 cherry


tasks = ["study", "exercise", "sleep"]
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
  #prints:
  #1 study
  #2 exercise
  #3 sleep

# gives scores to people
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
#grades = [B+, A, B]

for name, score in zip(names, scores):
    print(name, score)# can add list
#Alice 85    #B+
#Bob 90      #A
#Charlie 78  #B

#convert zip result to list
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

pairs = list(zip(letters, numbers))
print(pairs)
#[('A', 1), ('B', 2), ('C', 3)]

#enumerate and zip together:
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i}. {name} scored {score}")
#1. Alice scored 85
#2. Bob scored 90
#3. Charlie scored 78
