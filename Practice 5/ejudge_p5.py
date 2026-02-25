#1
import re

txt = str(input())
if re.match("Hello", txt):
    print("Yes")
else: print("No")

#2
import re

txt = str(input())
tx2 = str(input())

if re.search(tx2, txt):
    print("Yes")
else: print("No")

#3
import re

txt = str(input())
tx2 = str(input())
count = 0
count = re.findall(tx2, txt)

print(len(count))

#4
import re

txt = str(input())
x = re.findall("\d", txt)

print(" ".join(x))

#5
import re

txt = str(input())

if re.search("^[a-zA-Z]+\d+$", txt):
    print("Yes")
else: print("No")

#6
import re

txt = str(input())

x = re.split("\s", txt)
found = False
s = []

for n in x:
    if not found:
        if re.search("^.+@.+\.", n):
            s = n
            found = True

if not found:
    print("No email")
else:
    print(s)

#7
import re

txt = str(input()) # full string
tx2 = str(input()) # replaced character
tx3 = str(input()) # the replacer

x = re.sub(tx2, tx3, txt)
print(x)

#8
import re

txt = str(input()) # full string
tx2 = str(input()) # regex chars

x = re.split(tx2, txt)
print(",".join(x))

#9
import re

txt = str(input()) # full string
x = re.split('\s', txt)
count = 0
for i in x:
    if len(i) == 3:
        count += 1

print(count)

#10
import re

txt = str(input()) # full string

if re.search("cat|dog", txt):
    print("Yes")
else: print("No")

#11
import re

txt = str(input()) # full string

x = re.findall("[A-Z]", txt)

count = 0
for i in x:
    count+= 1
print(count)

#12
import re

txt = str(input()) # full string
x = re.findall("\d\d+", txt)

print(" ".join(x))

#13
import re

txt = str(input()) # full string
x = re.findall("\w+", txt)

count = 0
for i in x:
    count+= 1
print(count)

#14
import re

txt = str(input()) # full string
pattern = re.compile("^\d+$")

if pattern.fullmatch(txt):
    print("Match")
else:
    print("No match")

#15
import re

txt = str(input()) # full string
def double_digit(match):
    return match.group() * 2

x = re.sub("\d", double_digit, txt)
print(x)

#16
import re

txt = str(input()) # full string

pattern = "Name:\s*(.+), \s*Age:\s*(.+)"
match = re.search(pattern, txt)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)

#17
import re

txt = str(input()) # full string

pattern = "\d\d/\d\d/\d+"
match = re.findall(pattern, txt)

count = 0
for i in match:
    count+= 1
print(count)

#18
import re

txt = str(input()) # full string
tx2 = str(input())

x = re.findall(".", txt)

count = 0
for i in x:
    if tx2 == i:
        count += 1
print(count)

#alt 18
import re

text = input()
pattern = input()

escaped_pattern = re.escape(pattern)

matches = re.findall(escaped_pattern, text)

print(len(matches))

#19
import re

txt = str(input()) # full string

x = re.compile(txt)
y = re.split("\s", txt)

count = 0
for i in y:
    count += 1
print(count)

#alt 19
import re

txt = input()

# Compile pattern to match a word
pattern = re.compile(r'\b\w+\b')

# Find all matches
words = pattern.findall(txt)

# Count them
print(len(words))
