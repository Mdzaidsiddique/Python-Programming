# sets are used to store multiple value in a single variable
# unchangable : *Set items are unchangeable, but we can remove items and add new items
# unordered: the items in set do not have defined order
# no duplicates: Sets cannot have two items with the same value.

my_set = {"md zaid", 45, "Python", 45}
print(my_set) #{'Python', 45, 'md zaid'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
# 1 and True and 0 and False consider same value in sets 
print(thisset) #{'banana', 2, 'cherry', True, 'apple'}

# length: len()
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}
print(type(set1)) #<class 'set'>

# set() constructor :: note double bracket
set2 = set(("apple", "banana", "cherry"))
print(set2)
