# A variable is only available from inside the region it is created. This is called scope.

x = 300 # This is global scope

def myFunc():
  y = 400 # This is local scope
  print(x)
  print(y)

myFunc()

print(x)