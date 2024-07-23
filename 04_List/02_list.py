## CHANGES: lists are mutable, that menas we can change
thislist = ["apple", "banana", "cherry"]
thislist1 = thislist
thislist[2] = "kiwi"

print(thislist)  #['apple', 'banana', 'kiwi']
print(thislist1) #['apple', 'banana', 'kiwi']

# change range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["papaya", "berry", "pineapple"]

print(thislist) #['apple', 'papaya', 'berry', 'pineapple', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

# since endRange is exclusive so if we provide more value at less place then it will adjust
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

### INSERT: insert(index, new_element) at sp. index and shift other element accordingly
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "pineapple")
print(thislist) #['apple', 'banana', 'pineapple', 'cherry']


### ADD 
# append(): To add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("mango")
print(thislist) #['apple', 'banana', 'cherry', 'mango']

# insert(index, item): to insetrt item at sp. index
thislist.insert(0, "orange")
print(thislist) #['orange', 'apple', 'banana', 'cherry', 'mango']

### Remove: Specified Item
# remove(item): it will remove the specified item form the list
# if there are more than one specified values are present in list, first occurance will remove
removedItem = thislist.remove("orange")
print(removedItem) #None
print(thislist) #['apple', 'banana', 'cherry', 'mango']

# Remove: Specified Index
# pop(index)
# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist) #['banana', 'cherry']

#  del: The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist) #['apple', 'banana']


# Clear(): clear the list : all the elements will remove but list structure would be there
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]