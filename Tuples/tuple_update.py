# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #('apple', 'kiwi', 'cherry')

# Add items: Convert to list, add, then convert back to tuple
t1 = (1,2,43,5)
l1 = list(t1)
l1.append(60)
t1 = tuple(l1)

print(t1) #(1, 2, 43, 5, 60)

# Add tuple to a tuple : +=
t1 = (1,2,3)
t2 = (4,)

t1+=t2
print(t1) #(1, 2, 3, 4)

#removing items

# 1st approach: tuple to list, remove from list, convert back to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# 2nd Approach: del keyword (it will remoive tuple completely)

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists