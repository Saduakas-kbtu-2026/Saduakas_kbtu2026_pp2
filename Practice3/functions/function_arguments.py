def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus") 

def my_function2(name): # name is a parameter
  print("Hello", name)

my_function2("Emil") # "Emil" is an argument 

def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes") 


def country(country = "Norway"):
  print("I am from", country)

country("Sweden")
country("India")
country()
country("Brazil") 

def my_pet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_pet(animal = "dog", name = "Buddy") #this way order of arguments doesnt matter
my_pet(name = "Buddy", animal = "dog") 
