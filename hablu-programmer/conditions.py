# if else
A = 33
B = 200
if B > A:
  print("B is greater than A")
else:
  print("A is greater than B")

# else if (elif)
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# Short Hand if else
a = 200
b = 33
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# TITLE: Logical Operator
# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
# Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# TITLE: Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass statement
a = 33
b = 200

if b > a:
  pass