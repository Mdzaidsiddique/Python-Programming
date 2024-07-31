# enumerate(iterable, startIndex=0 or 1) is a built-in function that allows you to iterate over a iterable and have an automatic counter. 

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)