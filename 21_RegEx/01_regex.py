# Regular Expression: a sequence of characters that forms a search pattern

import re

# (1) search - Returns a Match object if there is a match anywhere in the string
txt = "Consistency is the Key."
x = re.search("not", txt)
print(x) # if there is no match the value None wwill be returned instead of Match Object

txt = "The rain in Spain"
x = re.search("\s", txt) #\s: white space

print(x, ": ",  x.start(), x.end()) 


# (2) findall -	Returns a list containing all matches
print(re.findall("ai", txt)) #['ai', 'ai']


# (3) split - Returns a list where the string has been split at each match
result = re.split("\s", txt) #split at each whitespace character
print(result) # ['The', 'rain', 'in', 'Spain']



# (4) sub -	Replaces one or many matches with a string
txt = "The rain in Spain"
x = re.sub("\s", "-", txt)
print(x) #The-rain-in-Spain
