# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Title: Class & Object
class studentInfo:
  name = ""
  age = ""
  id = ""

# These are objects
stu1 = studentInfo()
stu2 = studentInfo()
stu3 = studentInfo()

stu1.name = "Shaimon"
stu1.age = 20
print(stu1.name, stu1.age)