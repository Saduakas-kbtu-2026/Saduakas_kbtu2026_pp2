class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")
    
    def __str__(self):#custom method, specifies what to do when obj is printed
        return f"{self.name} ({self.age})"

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday() 

print(p1)

