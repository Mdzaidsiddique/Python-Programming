import copy
# deep copy

original = [1,2,[3,4], [5,6]]

"""
deep copy means it creates fully independent copies of all nested objects, 
so changes made to the copied structure won't affect the original and vice versa.
"""

deep_copy = copy.deepcopy(original)

deep_copy[2][0] = 200  #change will reflect only in deep_copy

print(original, deep_copy)

original[2][0] = 300 #only reflect in original not in deep copy
print(original, deep_copy)