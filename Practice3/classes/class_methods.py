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
    
    def __str__(self):#custom method, specifies what to do when obj is printed
        return f"{self.name} ({self.age})"


# Create an object
p1 = Person("John", 36, "Ontario", "Canada")
# Call the greet method
p1.greet()
#Hello, my name is John I am 36

p2 = Person("Clark")
p2.display_info()


class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) 

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs() 

del Person.__str__() # deletes __str__() method
