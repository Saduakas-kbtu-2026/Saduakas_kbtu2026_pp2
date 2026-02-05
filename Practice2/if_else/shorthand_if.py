a = 5
b = 2
if a > b: print("a is greater than b") # oneline if statement

a = 2
b = 330
print("A") if a > b else print("B") # shorthand if else

a = 10
b = 20
bigger = a if a > b else b # assiging a value with shorthand if else
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 
#multiple conditions in one line
#prints A if a>b
#else if a==b prints = 
#else prints B
