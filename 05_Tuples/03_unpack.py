# when we create tuple we normally assign value to it: this is called "packing" a tuple
fruits = ("apple", "banana", "cherry") # packing a tuple

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

green, yellow, red = fruits

print(green) #apple
print(yellow) #banana
print(red) #cherry

# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.