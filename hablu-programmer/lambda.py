# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax=> lambda arguments : expression

def sumFunc(a,b):
  print(a+b)

sumFunc(20,10)

# lambda function
x = lambda a,b: a+b
print(x(50,10))