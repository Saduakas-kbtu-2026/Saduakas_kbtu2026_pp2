class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

class Student(Person):#student is subclass of person
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 

p1 = Student("Mike", "Olsen")
p1.printname() 
