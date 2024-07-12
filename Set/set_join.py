# True and 1 and 0 and False are same in sets
"""
- There are several ways to join two or more sets in Python.

- The union() and update() methods joins all items from both sets.

- The intersection() method keeps ONLY the duplicates.

- The difference() method keeps the items from the first set that are not in the other set(s).

- The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

# Union: The union() method returns a new set with all items from both sets.
set1 = {1,2,3,4}
set2 = {"a", "b", "c"}

set3 = set1.union(set2)
print(set3) #{1, 2, 3, 4, 'b', 'c', 'a'}
print(set1) #{1, 2, 3, 4}

# we can use | operator insted of union(): both will give same result
set1 = {1,2,3,4}
set2 = {"a", "b", "c"}
set3 = set1 | set2
print(set3) #{1, 2, 3, 4, 'b', 'a', 'c'}

# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# my_set = set1.union(set2, set3, set4)

# when using the | operator, separate the sets with more | operators:
my_set = set1 |set2 | set3 | set4
print(my_set) #{1, 2, 'a', 3, 'bananas', 'cherry', 'apple', 'c', 'Elena', 'b', 'John'}

# with the help of union we can join set with list, tuple as well
set = {1,2,3}
tuple = ("zaid", 45, True)
list = ["alif", 45, False, 0]

my_set = set.union(tuple, list)
print(my_set) #{False, 1, 2, 3, 'alif', 'zaid', 45}

# my_set = set | tuple | list
# Note: The | operator only allows to join sets with sets, not with other data types like union()

# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #{'a', 1, 2, 'c', 'b', 3}

# Note: Both union() and update() will exclude any duplicate items.


# Intersection: Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

my_set = set1.intersection(set2)
print(my_set) #{"apple"}

# You can use the & (for only set with set) operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
my_set = set1 & set2
print(my_set) #{'apple'}

# intersection_update(): keep common items from both sets but change in original set, not return new one
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) #{'apple'}
print(set2) #{'microsoft', 'google', 'apple'}

# Difference: The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)

print(set3) #{'cherry', 'banana'}

# we can use - operator (only set with set) instead of difference: both will give same result
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1-set2
print(set3) #{'cherry', 'banana'}

# difference_update(): it will also keep the items that are not present in both sets, but never return new set, change in original one
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)

print("du : ",set1) #du :  {'cherry', 'banana'}

# symmetric difference: (uncommon items of both sets)
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# keep the item that are not present in both the sets, return new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3) #{'microsoft', 'banana', 'google', 'cherry'}

# ^ operators instead of symmetric_difference() but it is allow for sets with sets only not fot other data types (like tuples and list)
set4 = set1 ^ set2
print(set4)

# symmetric_difference_update() also to keep the items that are not present in both sets:
# change original set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print("sdu", set1) #sdu {'banana', 'cherry', 'microsoft', 'google'}
