# numeric data type
x = 20
y = 20.5
z = 10j

print(type(z))

# string data type
firstName = "Al"
lastName = "Shaimon"

print("My name is " + firstName + " " + lastName)

# Boolean data type
X = 8
Y = 10
print(X > Y)

# Binary data type
# bytes (this is immutable i.e we can't change it)
list = [1,2,3,4,5,4,6,4,6,65,65,65,96,9,255]
b = bytes(list)

print(type(b))

# bytearray (this is mutable i.e we can change it)
list2 = [1,2,3,4,5,4,6,4,6,65,65,65,96,9,255]
b2 = bytearray(list2)

print(type(b2))

# NoneType data type
x = None

print(type(x))

# Sequence data type
# list (this is mutable)
li = ['karim', 'rahim', 'hakim']
li[0] = 'bakim'

print(li)

# tuple (this is immutable)
tup = (5,10,15,20,25)
# tup[0] = 69 =>this will not work because tuple is immutable

print(tup)

# range
ran = range(6)

for i in ran:
  print(i)