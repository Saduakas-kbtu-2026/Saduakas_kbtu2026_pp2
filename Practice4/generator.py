import math
 
def fun(max):#sqrt of number
    cnt = 1
    while cnt <= max:
        yield pow(cnt, 2)
        cnt += 1
 
N = fun(int(input()))
for n in N:
    print(n)

#even numbers
def even_num(max):
    for i in range(0,max+1,2):
        yield i
inp = int(input())
 
first_e = True
for num in even_num(inp):
    if not first_e:
        print(",", end="")
    print(num, end="")
    first_e = False

#divisable by 3 and 4
def divisable(max):
    for i in range(0,max+1, 12):
        yield i

div_num = int(input())
for num in divisable(div_num):
    print(num, end="")
    print(" ", end="")

#makes 2^n squares
import math
def square(min, max):
    for i in range(min, max+1):
        yield pow(i, 2)
 
sq_inp = list(map(int, input().split()))
 
for num in square(sq_inp[0], sq_inp[1]):
    print(num)

#from n to 0
def reducer(num):
    for i in range(num+1):
        yield num - i
 
n = int(input())
 
for num in reducer(n):
    print(num)
