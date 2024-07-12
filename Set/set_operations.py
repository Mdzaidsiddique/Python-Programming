# Access Set Items: can't access set by index (unordered)

set1 = {"apple", "banana", "cherry"}

for x in set1:
    print(x)

# check "banana" is present in set or not
print("banana" in set1) # True

# check not present
print("litchi" not in set1) #True

#change items: once set is created we can't change its item but add/ remove

# add()
set2 = {"apple", "banana", "cherry"}
set2.add("litchi")
print(set2)

# update(): add item from another set to current set
set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set.update(tropical)

print(set) #{'apple', 'papaya', 'pineapple', 'cherry', 'mango', 'banana'}

# add any iterable: update()
set = {"apple", "banana", "cherry"}
list = ["kiwi", "orange"]

set.update(list)
print(set) #{'orange', 'cherry', 'banana', 'kiwi', 'apple'}


# Remove set items: remove() or discard()
# remove(): #Note: If the item to remove does not exist, remove() will raise an error.
set = {"apple", "banana", "cherry"}
set.remove("banana")
print(set) #{'apple', 'cherry'}

# discard(): # Note: If the item to remove does not exist, discard() will NOT raise an error.
set.remove("apple")
print(set) #{'cherry'}

# pop(): You can also use the pop() method to remove an item, but this method will remove a random item, 
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The return value of the pop() method is the removed item.
set = {"apple", "banana", "cherry"}
x = set.pop()
print(x)

# clear(): empty the set
set = {1,2,3,4,5}
set.clear()
print(set) #set()

# del: the del keyword will delete the set entirly
set = {1,2,35,66}
print(set)
del set
print(set) # <class 'set'>

# since set are unordered (no index) hence only for loop will work
set = {1,2,35,66, "zaid", 45, "male", True}
for x in set:
    print(x)
