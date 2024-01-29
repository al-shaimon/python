
# Title: Module import method 1
# Use import than module file name
import module

module.greeting("Shaimon")

# Title: Method 2
# You can create an alias when you import a module, by using the as keyword:
import module as m

a = m.person1["age"]
print(a)

# Title: Method 3
from module import person1
print(person1["name"])