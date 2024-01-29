# using __ before variable we can make it private encapsulation
class Parent:
  def __init__(self, Name, Age):
    self.__Name = Name
    self.Age = Age
    print(self.__Name)
p1 = Parent("Shaimon", "20")

print(p1.Name)