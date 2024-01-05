li = [1,2,3]

li[2] = 4

print(li)
print(li[0])
print(type(li))

lis = ['karim', 'rahim', 'hakim']

print(lis)
print(type(lis))

lib = [True, False, False, True]

print(lib)
print(type(lib))
print()

# Access list items
cv = ['name', 'phone', 'projects', 'portfolio', 'social media']

print(cv)
print(cv[1])
print(cv[3])
print(cv[4])
print()

# Change list items
cv[1] = 'email'
cv[4] = 'linkedin'

print(cv)
print(cv[1])
print(cv[4])
print()

# Add List items ( append() , insert() )
# append()
cv.append('experiences')

print(cv)

# insert()
cv.insert(1, 'id')

print(cv)
print()


# Remove List items ( remove() , pop() , del() , clear() )
# remove()
fruits = ['mango', 'banana', 'orange', 'apple']

fruits.remove('banana')

print(fruits)

# pop()
fruits.pop(0)

print(fruits)

# del()
del fruits[1]

print(fruits)

# clear()
fruits.clear()

print(fruits)
print()


# Loop Lists ( for loop, while loop )
# for loop
loopList = ['a', 'e', 'i', 'o', 'u']
for i in loopList:
  print(i)
  
for i in range(len(loopList)):
  print(i)

print()

# while loop
loopList = ['a', 'e', 'i', 'o', 'u']
y = 0
while y < len(loopList):
  print(loopList[y])
  y = y + 1

print()


# List Comprehension
numbers = [1,2,3,4,5]
squares = [num**2 for num in numbers]

print(squares)
print()


# Sort List
# Acceding sort 
numbers = [5,9,4,5,2,3,8,4,8,9,5,1,2,0,4]
numbers.sort()
print(numbers)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print(vowels)

# Descending sort
numbers = [5,9,4,5,2,3,8,4,8,9,5,1,2,0,4]
numbers.sort()
print(numbers)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print(vowels)

# Reverse sort
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.reverse()
print(vowels)
print()


# Copy a List
list1 = ['apple', 'orange', 'banana', 'mango']
list2 = list1.copy()
print(list2)
print()

# Join Two Lists
list1 = ['a', 'b', 'c']
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

# Append Two Lists
list1 = ['a', 'b', 'c']
list2 = [1,2,3]

for x in list2:
  list1.append(x)

print(list1)

# Extend Two Lists
list1 = ['a', 'b', 'c']
list2 = [1,2,3]

list1.extend(list2)
print(list1)