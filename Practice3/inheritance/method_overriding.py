# Python program to demonstrate 
# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		super().__init__()  # Call parent constructor
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"

class Person:
    def __init__(self, fname, lname): # this is method overriding
        self.firstname = fname
        self.lastname = lname

    def __printname(self): # private mehotd cannot be called in main
        print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # makes child inherit all properties and methods of parent
    self.graduationyear = 2019

