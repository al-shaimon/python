# There are three type of methods available
# 1. Instance method
# 2. Class Method
# 3. Static Method

class ClassName:
  def InstanceMethod(self):
    print("Hello Instance Method")
  @classmethod
  def ClassMethod(cls):
    print("This is Class Method")
    
  @staticmethod
  def StaticMethod():
    print("This is Static Method")
  
v1 = ClassName()
v1.InstanceMethod()

v1.ClassMethod()

v1.StaticMethod()