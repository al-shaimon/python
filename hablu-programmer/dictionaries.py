# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
studentInfo = {
  "shaimon" : {
    "name": "Shaimon",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "C231139",
    "phoneNumber": "+8801690174668",   
  },
  "x" : {
    "name": "x",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "12345",
    "phoneNumber": "+880123456789"
  },
}

# TITLE: Accessing Items
# print(studentInfo["shaimon"]["id"])
# print(studentInfo.get("x"))
# print(studentInfo.keys())
# print(studentInfo.values())

# TITLE: Change Values
studentInfo = {
  "shaimon" : {
    "name": "Shaimon",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "C231139",
    "phoneNumber": "+8801690174668",   
  },
  "year" : 1999,
}

studentInfo["year"] = 2005

# print(studentInfo["year"])

# TITLE: Update Values
studentInfo.update({"shaimon" : "Shaimon is a web developer :-)"})

# print(studentInfo["shaimon"])

# TITLE: Remove Items
# pop()
studentInfo = {
  "shaimon" : {
    "name": "Shaimon",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "C231139",
    "phoneNumber": "+8801690174668",   
  },
  "x" : {
    "name": "x",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "12345",
    "phoneNumber": "+880123456789"
  },
}

studentInfo.pop("x")
# print(studentInfo)

# popitem() will remove last item
thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisDict.popitem()
# print(thisDict)

# del
thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisDict["model"]
# print(thisDict)

# clear()
thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisDict.clear()
# print(thisDict)

# TITLE: Loop
studentInfo = {
  "shaimon" : {
    "name": "Shaimon",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "C231139",
    "phoneNumber": "+8801690174668",   
  },
  "x" : {
    "name": "x",
    "location": "CTG",
    "study": "B.Sc in CSE",
    "semester": "3rd",
    "id": "12345",
    "phoneNumber": "+880123456789"
  },
}
# Print all key names in the dictionary, one by one:
for i in studentInfo:
  print(i)
  
# Print all values in the dictionary, one by one:
for i in studentInfo:
  print(studentInfo[i])

for i in studentInfo.values():
  print(studentInfo)

# We can use the keys() method to return the keys of a dictionary:
for i in studentInfo.keys():
  print(studentInfo)
  
# Loop through both keys and values, by using the items() method:
for i in studentInfo.items():
  print(i)
  
# TITLE: Copy a Dictionaries
# copy()
oldDict = {
  "a": "A",
  "b": "B",
  "c": "C",
}

newDict = oldDict.copy()
print(newDict)

# dict()
newDict = dict(oldDict)
print(newDict)

# TITLE: Dictionary Methods
# clear(): Removes all the elements from the dictionary
# copy(): Returns a copy of the dictionary
# fromkeys(): Returns a dictionary with the specified keys and value
# get(): Returns the value of the specified key
# items(): Returns a list containing a tuple for each key value pair
# keys(): Returns a list containing the dictionary's keys
# pop(): Removes the element with the specified key
# popitem(): Removes the last inserted key-value pair
# setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update(): Updates the dictionary with the specified key-value pairs
# values(): Returns a list of all the values in the dictionary