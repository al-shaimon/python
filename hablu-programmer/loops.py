# While loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 0
while i < 10:
  print(i)
  i += 1

# break and continue
# break
i = 1
while i < 10:
  print(i)
  if i == 3:
    break
  i += 1

# continue
i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)
  
# else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]

for i in fruits:
  print(i)
  if i == "banana":
    break