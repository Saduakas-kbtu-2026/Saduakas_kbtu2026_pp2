#OOP
class MyClass: #can think of it as a type of object
    x = 5 # attributes | the paint of a car | memory of computer 

p1 = MyClass() #assigning p1 object with class
p2 = MyClass()
p3 = MyClass()
#Each object is independent and has its own copy of the class properties.
print(p1.x) # printe the value of p1s x value

del p1 # deletes object p1
