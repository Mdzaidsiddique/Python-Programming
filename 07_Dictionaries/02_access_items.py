my_dict = {
    "name" : "zaid alif siddique",
    "age" : 34,
    "gender" : "male",
    "coding" : True,
    "languages" : ["python", "Java", "JavaScript", "HTML", "SQL"]
}

# access items by keyname
print(my_dict["languages"]) #will raise KeyError if key not found

# by get(key, default) method, No error raised, None, if key not found also default value can be provided
language_known = my_dict.get("language")

# key(): return list of all the keys in the dictionary ('dict_keys' types)
keys = my_dict.keys()
print(keys, type(keys)) #dict_keys(['name', 'age', 'gender', 'coding', 'languages']) <class 'dict_keys'>

# values(): The values() method will return a list of all the values in the dictionary. ('dict' type)
values = my_dict.values()
print(values, type(my_dict))


#items(): return each item in a dictionary, as tuples in a list.
items = my_dict.items()
print(items, type) # [(k,v),(k,v),(k,v)] <class 'type'>


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# Add a new item to the original dictionary, 
# and see that the keys list, value list and item list will get updated as well:

keys = car.keys()
values = car.values()
items = car.items()

#before the change:
print(keys)
print(values)
print(items)

car["color"] = ["white", "red", "black"] # added new item(key:value)

#after the change: keys, values and item list will get updated dynamicaaly
print(keys)
print(values)
print(items)


# chekc if key exists
if "color" in car:
    print("Yes, different colors are available")


