import copy

list = [1,2,[3,4], [5,6]]

# shallow copy 
"""
A shallow copy of an object creates a new object, but does not create copies of the objects that the original object contains. 
Instead, it copies references to those objects. As a result, both the original and the copied objects share the same nested objects.
This means that modifications to nested objects in the copied object will be reflected in the original object, and vice versa.
"""
list2 = list
print(list is list2) #True

shallow_copy = copy.copy(list)
print(copy is shallow_copy) #False

shallow_copy[2][0] = 100
list[0] = 1000 #changes only reflect in list

print(list, list2, shallow_copy) #change will reflect in all the copies


# deep copy

"""
A deep copy of an object creates a new object and recursively copies all objects that the original object contains.
This means that the new object is completely independent of the original object.
Modifications to the nested objects in the copied object will not affect the original object, and vice versa.
"""
list = [1,2,[3,4], [5,6]]
list2 = list
deep_copy = copy.deepcopy(list)
deep_copy[2][0] = 200
print(deep_copy) #change will reflect in only deep_copy
print(list)
print(list2)

list[2][0] = 300 #only reflect in list not in deep copy
print(deep_copy)