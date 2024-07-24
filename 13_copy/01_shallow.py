import copy

list = [1,2,[3,4], [5,6]]

# assignment (references share only)
list2 = list
print(list is list2) #True

# shallow copy 
"""
Shallow copy create new objects but insert references into the objects found in original one, this means that 
the modifications to nested objects in the copied object will be reflected in the original object, and vice versa.
"""

shallow_copy = copy.copy(list)
print(copy is shallow_copy) #False

shallow_copy[2][0] = 100 #change will reflect in all the copies
list[0] = 1000 #changes only reflect in list not in shallow_copy

print(list, list2, shallow_copy) 
