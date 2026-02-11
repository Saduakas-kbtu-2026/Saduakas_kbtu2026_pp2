x = lambda a : a + 10 #is basically a 1 line function, useful for math operations
# end-variable = lambda var1, var2, ..., varN : (operation) with vars
print(x(5)) 

y = lambda a, b : a * b
print(y(5, 6))  #30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # 5+6+2 = 13

#power of lambda
def myfunc(n):
  return lambda a : a * n # 2a

mydoubler = myfunc(2)
print(mydoubler(11)) # 22

mytripler = myfunc(3)
print(mytripler(11)) # 33
