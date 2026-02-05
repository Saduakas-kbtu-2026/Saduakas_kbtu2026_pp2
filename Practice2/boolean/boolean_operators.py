class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # False

def myFunction() :
  return True

print(myFunction()) #true


def myFunction1() :
  return True

if myFunction1(): #prints this
  print("YES!")
else:
  print("NO!") 

z = 200
print(isinstance(z, int)) #true
