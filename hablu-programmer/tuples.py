# Tuple is unchangeable
NewTuples = (1,2,3,'shaimon', 6544)

print(type(NewTuples))

# NewTuples[1] = 20

# print(NewTuples)

# TITLE: Negative Indexing

print(NewTuples[-1]) # -1 refers to the last item, -2 refers to the second last item etc.

# TITLE: Range of Indexes

print(NewTuples[0:4]) # Note: The search will start at index 0 (included) and end at index 4 (not included).

# TITLE: Update Tuples
# Tuple is immutable. To update tuples:
# 1. Convert it to list
# 2. Append data to list
# 3. Convert list to tuple

vowels = ('a', 'e', 'i', 'o');
updatedVowels = list(vowels)
updatedVowels.append('u')
vowels = tuple(updatedVowels)

print(vowels)

# TITLE: Unpack Tuples

fruits = ("apple", "banana", "cherry","dates","eggplant")
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
(a,b,*c) = fruits

print(a) # Output: apple
print(b) # Output: banana
print(c) # Output: ['cherry', 'dog', 'egg']

# TITLE: Loop Tuples
# For Loop
fruits = ("apple", "banana", "cherry",'dates','eggplant')

for i in fruits:
  print(i)

# Range
for x in range(len(fruits)):
  print(fruits[x])
  
# While loop
fruits = ("apple", "banana", "cherry",'dates','eggplant')

i = 0
while i < len(fruits):
  print(fruits[i])
  i+=1
  
# TITLE: Join Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ('a', 'b', 'c', 'd')
tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2

print(tuple3)

# TITLE: Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
tuple = (1,2,3,4,5)
multiplyTuple = tuple * 2

print(multiplyTuple)

# TITLE: Tuple Methods
# Python has two built-in methods that you can use on tuples.
# 1) count() => Returns the number of times a specified value occurs in a tuple
# 2) index() => Searches the tuple for a specified value and returns the position of where it was found

# count()
fruits = ("apple", "banana", "banana",'dates','banana')
counting = fruits.count("banana") # Output: 3

print(counting)

# index()
fruits = ("apple", "banana", "cherry",'dates','eggplant')
indexing = fruits.index("cherry")

print(indexing) #Output: 2