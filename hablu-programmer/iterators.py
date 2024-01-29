# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

list = [1,2,3,4,5,6,7,8,9]
x = iter(list)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))