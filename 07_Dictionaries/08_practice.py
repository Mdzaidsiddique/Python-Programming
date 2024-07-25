# merge two dictionary

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# merged_dict = {**dict1, **dict1} #have to read about this
dict1.update(dict2)

# print(dict1)

# dict1.clear()
dict1.pop("a")
print(dict1)