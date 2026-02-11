def my_function():
    print("Hello from a function") 

my_function()

def fahrenheit_to_celsius(fahrenheit): # helps avoid repetition
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) 
#can also be written as
print(get_greeting())
