def fahrenheit_to_celsius(fahrenheit): # helps avoid repetition
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

def math(x, y):
  return x + y

result = math(5, 3)
print(result) 

def my_fruits():
  return ["apple", "banana", "cherry"]

fruits = my_fruits()
print(fruits[0])
print(fruits[1])
print(fruits[2]) 

def equalto():
  return (10, 20)

x, y = equalto()
print("x:", x)
print("y:", y) 

#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) 
