# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruit_list = ["apple", "banana", "orange", "mango"]

new_fruit_list = []

for fruit in fruit_list:
    new_fruit_list.append(fruit)

print(new_fruit_list)

# With list comprehension we can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruit_list = [x for x in fruits]
print("-=-=-=-=-=-=-=-=----=-=-")
print(new_fruit_list)

new_fruit_list2 = [x for x in fruits if "a" in x] #elements that contain 'a' will added in new list
print(new_fruit_list2)

# newlist = [expression for item in iterable if condition == True]
# return new list and leaving older one unchanged
# The iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in fruits if x != "apple"]

#  we can use range()
newlist = [x for x in range(10)] # 0 to 9 in list
print(newlist)

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]


list  = [x*10 for x in range(10) if x<5]
print(list)