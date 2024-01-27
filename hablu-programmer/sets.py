# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# * Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# * Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
MySet = {1, False, 0, True, 'string', 'string'}

print(MySet)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
thisSet = {"apple", "banana", "cherry"}
print(thisSet)

print(len(MySet))
print(len(thisSet))

# TITLE: Access Set Items
MySet = {1,2,5,4,3,6,9,8,7}

for i in MySet:
  print(i)

print(3 in MySet)

# TITLE: Add Set Items
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

print(fruits)

# TITLE: Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)

MySet = {"apple", "banana", "cherry"}
MyList = ["kiwi", "orange"]
MyTuple = (1,2,3,4)

MySet.update(MyList, MyTuple)

print(MySet)

# TITLE: Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
# remove()
#? Note: If the item to remove does not exist, remove() will raise an error.
MySet = {"apple", "banana", "cherry"}
MySet.remove("banana")

print(MySet)

# discard()
#? Note: If the item to remove does not exist, discard() will NOT raise an error. 
MySet = {"apple", "banana", "cherry"}
MySet.discard("banana")

print(MySet)

# pop()
# Remove a random item by using the pop() method:
#? Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
MySet = {"apple", "banana", "cherry"}
MySet.pop()

print(MySet)

# clear()
# The clear() method empties the set:
MySet = {"apple", "banana", "cherry"}
MySet.clear()

print(MySet)

# del 
# The del keyword will delete the set completely:
MySet = {"apple", "banana", "cherry"}
del MySet

# print(MySet) # will through error ('MySet' is not defined) because set deleted

# TITLE: Loop Sets
MySet = {"apple", "banana", "cherry"}
for i in MySet:
  print(i)
  
# TITLE: Join Sets and Set Methods
# union()
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update()
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#? Note: Both union() and update() will exclude any duplicate items. 

# intersection_update()
#? The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# intersection()
#? The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

# symmetric_difference_update()
#? The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

# symmetric_difference()
#? The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

