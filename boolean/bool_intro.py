x = "Hello"
y = 15

print(bool(x)) #True
print(bool(y)) #True

print(bool("abc"))                          #True
print(bool(123))                            #True
print(bool(["apple", "cherry", "banana"]))  #True

#"empty" values are false, for example:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
# is all False

