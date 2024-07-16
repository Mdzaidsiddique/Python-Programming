my_dict = {
    "name" : "zaid alif siddique",
    "age" : 34,
    "gender" : "male",
    "coding" : True,
    "languages" : ["python", "Java", "JavaScript", "HTML", "SQL"]
}

# Print all key names in the dictionary, one by one:
for item in my_dict:
    print(item)

# using keys() method to return keys of a dictionary
for item in my_dict.keys():
    print("keys", item)

# Print all value one by one:
for item in my_dict:
    print(my_dict[item])

# using values() method to return values of a dictionary
for x in my_dict.values():
    print(x)


# Loop through both keys and values, by using the items() method:
for key, value in my_dict.items():
    print(key," : ", value)
