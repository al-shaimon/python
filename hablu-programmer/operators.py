# Arithmetic Operators (+, - , * , /, %, //, **)
# Addition ( + )
x = 5
y = 10

print(x + y)

# Subtraction ( - )
print(x-y)

# Multiplication ( * )
print(x*y)

# Division ( / )
print(x/y)

# Modulus ( % )
print(x%y)

# Exponentiation ( ** )
print(x**y)

# Floor Division ( // )
sum1 = 15
sum2 = 2

print(sum1 // sum2)

print()


# Assignment Operators ( = , += , -= , *= , /= , %= , //= , **= , &= , |= , ^= , >>= , <<= )
a = 5
a += 10

print(a)

a*=10

print(a)

print()


# Comparison Operators ( == , != , > , < , >= , <= )
x = 5
y = 10

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print()


# Logical Operators ( and , or , not )
x = 10

print(x > 3 and x < 10)
print(x > 3 or x < 10)
print(not(x > 3 and x < 10))

print()


# Identity Operators ( is , is not )
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x is not y)
print(x == y)

print()


# Membership Operators ( in, not in )
x = ["apple", "banana"]

print("banana" in x)
print("apple" not in x)

print()


# Bitwise Operators ( & , | , ^ , ~ , << , >> )
print(3 << 2) # 3 means 0011 and 3 << 2 will become 1100 which is 12 in decimal