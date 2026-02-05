#numbers in python have a certain amount of inaccuracy to them.
#For example data type int cannot have a value less that -2,147,483,648 or
# greater than 2,147,483,647 in a 32-bit system or 9,223,372,036,854,775,807 and
# -9,223,372,036,854,775,808in a 64-bit system.
#Attempting to use such a number with int should result in a error.
i_int = int(9223372036854775808)
print(i_int)
#However, when presented with a number exceeding this maximum Python automatically
# converts it into the integer into a long datatype.
#Same is with floats, but floats suffer some inaccuracy with greater numbers
# or with small non-zero numbers like 0.0000000000340102. Especially when doing
# operations with floating points, due to floating point inaccuracy.
f_float = float(0.000000000000340102 + 0.000000000001200023)
print(f_float)
# it results in 1.5401250000000002e-12 which is technically incorrect; as the 
# 0.2e-27 should not be present.
c_complex = complex(1+2j)
print(c_complex) # complex numbers
