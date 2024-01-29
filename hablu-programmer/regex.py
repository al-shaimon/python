import re

text = "The rain in Spain"

a = re.findall("[a-z]", text)
print(a)

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# findall: Returns a list containing all matches
# search: Returns a Match object if there is a match anywhere in the string
# split: Returns a list where the string has been split at each match
# sub: Replaces one or many matches with a string

# https://www.w3schools.com/python/python_regex.asp