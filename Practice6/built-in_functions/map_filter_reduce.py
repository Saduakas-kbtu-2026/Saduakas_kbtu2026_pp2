from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)
#prints 15
#step by step proccess
#1 + 2 = 3
#3 + 3 = 6
#6 + 4 = 10
#10 + 5 = 15

#finds max number
from functools import reduce

numbers = [7, 2, 10, 4, 8]
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(maximum) # 10

#concentanate strings
from functools import reduce

words = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, words)

print(sentence) # Python is fun
