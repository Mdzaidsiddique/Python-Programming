# change value: we change the value of a specific item by referring to its key name:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# add item
car["year"] = 2024

print(car)

#update({k:v}): update the dictionay with the items provided as argument({k:v})
# if key exist it will update and if not then it will add

car.update({"year":2018})
car.update({"latest_model":"Mustang GT"})
print(car)

car1 = car.copy()
print("coppied car : ",car1, car is car1)

# remove item from dictionary
# 1) pop(key): remove item with specefied key name

car1.pop("latest_model")
print(car1)

# popitem(): remove last inserted item: before 3.7 it remove random item
car.popitem()
print("car : ", car)


# del keyword removes item with the specified key name:
del car1["brand"]

print(car1)

# del keyword can also delete the dictionary completely:
del car1
# print(car1) #error because "car1" no longer exists.


# clear(): it will empty the dictionary
car1 = car.copy()
car1.clear()

print(car1) #{}