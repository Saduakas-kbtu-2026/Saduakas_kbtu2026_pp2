#instead of 
##p1 = Person()
##p1.name = "Tobias"
##p1.age = 25
# we can automatically set all variables: with __init__()
##p1 = Person("Linus", 28)


# Create a class
class Person:
    #self does not have to be named self
    def __init__(self, name, age = 18, city = "Astana", country = "Kazakhstan"): #sets 18 as default if missing value
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def greet(self):
        print("Hello, my name is", self.name, "I am", self.age)

    def display_info(self):
        self.greet() # can call other methods inside of same class

        print(f"{self.name} {self.age} {self.city} {self.country}")

# Create an object
p1 = Person("John", 36, "Ontario", "Canada")
# Call the greet method
p1.greet()
#Hello, my name is John I am 36

p2 = Person("Clark")
p2.display_info()
