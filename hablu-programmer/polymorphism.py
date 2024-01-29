class Vehicle:
  def __init__(self, Model, Brand, Component):
    self.Model = Model
    self.Brand = Brand
    self.Component = Component
    
class Plane(Vehicle):
  pass

class Car(Vehicle):
  pass

p1 = Plane("Airbus A380", "Emirates", "All Component")
c1 = Car("BMW22", "BMW", "Main Component")

print(p1.Brand, p1.Model, p1.Component)
print(c1.Brand, c1.Model, c1.Component)