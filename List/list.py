#  List: Lists are used to store multiple items in a single variable.

# List items are ordered (new item placed at last), changeable (add, remove, change items), and allow duplicate values.

mylist = ["apple", "banana", "cherry"]

# can contain any datatypes
list1 = ["abc", 34, True, 40, "male"]

# len(): length
print(len(mylist)) #3

#type()
print(type(list1)) #<class 'list'>

# The list() Constructor
list2 = list((11,22,33,44)) # note the double brackets

print(list2, type(list2))

# // Accessing list item
list1 = ["abc", 34, True, 40, "male"]
print(list1[0], list1[-1])

# range of items [start():end(exclusive)]
print(list1[0:3]) #['abc', 34, True]
print(list1[:4]) # dtart from first value
list1[2:] # start from 2nd and go till end
list3 = list1[:] # create a copy (another reference) and assign to list3 

#range of negative indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']
print(thislist[-4:-8]) # []
print(thislist[-4:-6]) # []
print(thislist[-4:])   # ['orange', 'kiwi', 'melon', 'mango']

# in : to determine if element is present oe not
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "kiwi" in thislist:
    print("kiwi is present inside list")

# copy a list
# list2 = list1 pointed to a same object and changers will impact on both reference
list1 = [1,2,3]
list2 = list1

list3 = list(list1) # list() constructor

print(list1 is list2) #True
print(list1 is list3) #False

list4 = list1.copy() # .copy() method
print(list1 is list4) #False


# Join Lists
l1 = [1,2,3]
l2 = ['a','b','c']

l3 = l1+l2 # using + operator
print(l3)

for x in l2:
    l1.append(x) # append(): l2 items to l1

print(l1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2) #extend() method to add list2 at the end of list1
print(list1)








