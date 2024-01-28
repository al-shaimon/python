# Recursion is a common mathematical and programming concept. It means that a function calls itself
# def ReFunc():
#   print("recursion")
#   ReFunc()
  
# ReFunc()

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)