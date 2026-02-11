#*args and **kwargs allow functions to accept a unknown number of arguments.

#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:
def children(*kids):
    print("The youngest child is " + kids[2])

children("Emil", "Tobias", "Linus", "Phineas") 

def my_function1(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function1("Emil", "Tobias", "Linus") 

def my_function(greeting, *names): # hello is greetig, rest is *names
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") 

#practical example of *args
def summ(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(summ(1, 2, 3))
print(summ(10, 20, 30, 40))
print(summ(5)) 

def max_value(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(max_value(3, 7, 2, 9, 1)) 
print(max_value(3, 7, 2)) 


#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
def kids_name(**kid):
  print("His last name is " + kid["lname"])

kids_name(fname = "Tobias", lname = "Refsnes") 

def my_info(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_info(name = "Tobias", age = 30, city = "Bergen") 

def email_login(username, **details): # emil123 is username, everything else is kwarg
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

email_login("emil123", age = 25, city = "Oslo", hobby = "coding") 


def my_function3(a, b, c): #unpacks argument to tuple
  return a + b + c

numbers = [1, 2, 3]
result = my_function3(*numbers) # Same as: my_function(1, 2, 3)
print(result) 


def my_function4(fname, lname): #unpacks to dictionary
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function4(**person) # Same as: my_function(fname="Emil", lname="Refsnes") 
