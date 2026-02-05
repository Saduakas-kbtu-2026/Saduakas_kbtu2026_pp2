#strings
x = "Hello"
y = "World"
print(x + y) # HelloWorld
print(x, y) # Hello World
long_quote = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print( long_quote)

#slicing strings and modifying them
z = "Hello, World!"
print(z[:5]) #Hello
print(z[5:6]) #, 
print(z[7:])  #World!

print(z.upper()) # hello, world!
print(z.lower()) # HELLO, WORLD!
print(z.replace("H", "J")) #replace H with J | Jello, World!
print(z.split(",")) #['Hello', ' World!']
print(z , "I am using \"Python\" " ) # escape character | I am using "Python"

#f-strings
name = f"Peter"
surname = f"Parker"
print(f"Hello my name is {name} {surname}" + "!")
