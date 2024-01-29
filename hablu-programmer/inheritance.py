# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class: is the class being inherited from, also called base class.

# Child class: is the class that inherits from another class, also called derived class.

# This is Parent Class or Base Class
class father():
  car = "BMW"
  money = "100Cr"
  home = "2"

# This is Child Class 
class son(father):
  brokenCar = ""
  noMoney = ""
  noHome = ""
  
s = son()
# print(s.car)

# Title: Multiple inheritance

class father:
  car = "BMW"
  money = "100Cr"
  home = "2"

class son1:
  laptop = "MacBook pro"
  pc = "i5 14th gen"
  
class son2(father, son1):
  price = ""
  
m = son2()
# print(m.car, m.pc)

# Title: Multilevel inheritance

class father:
  car = "BMW"
  money = "100Cr"
  home = "2"

class son1(father):
  laptop = "MacBook pro"
  pc = "i5 14th gen"
  
class son2(son1):
  poor = ""
  
m = son2()
print(m.car, m.pc)

# Title: Hybrid and hierarchical inheritance

class father:
  car = "BMW"
  money = "100Cr"
  home = "2"

class son1(father):
  laptop = "MacBook pro"
  pc = "i5 14th gen"
  
class son2(son1, father):
  poor = ""

class son3(son2):
  veryPoor = "" 

m = son3()
print(m.car, m.pc)