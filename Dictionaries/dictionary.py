# stores data in key: value pairs
# ordered*(python 3.7), changeable and do not allow duplicates.
# In Python 3.6 and earlier, dictionaries are unordered.

my_dict = {
    "name" : "zaid alif siddique",
    "age" : 34,
    "gender" : "male",
    "coding" : True,
    "languages" : ["python", "Java", "JavaScript", "HTML", "SQL"]
}

print(my_dict) #{'name': 'zaid alif siddique', 'age': 34, 'gender': 'male', 'coding': True, 'languages': ['python', 'Java', 'JavaScript', 'HTML', 'SQL']}
# accessing element by key
print(my_dict["name"])
# print(my_dict["name", "age"]) #error


# Duplicate values will overwrite existing values:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(car) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# length: len()
print(len(my_dict))

#type() : dictionary are defined as Object with 'dict'
print(type(my_dict))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

the_dict = dict(name = "alif", age = 45, country = "India")
print(the_dict, type(the_dict))


# copy 
"""
we cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
# using copy()
car1 = car.copy()
print(car1 is car) # False

# using dict()
car2 = dict(car)
print(car2 is car) # False