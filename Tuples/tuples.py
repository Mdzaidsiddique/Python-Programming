# tuple: (ordered, unchangable, allow duplicates)

tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple)

# length: len()
print(len(tuple))

# creating tuple with one item 
t1 = ("apple",) # remember the comma
print(t1, type(t1))

not_tuple = ("apple") #string
print(not_tuple, type(not_tuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# tuple constructor : tuple(()) : double bracket is importnat
# t1 = tuple(("as","sd"))
# print(t1)

# Accessing tuples items (index, negative indexingf, range)
thistuple = ("apple", "banana", "cherry", "stbweey", "pineapple")
print(thistuple[0]) # apple
print(thistuple[-1]) #pineapple
print(thistuple[1:4]) #('banana', 'cherry', 'stbweey')
print(thistuple[-4:-1]) #start from -4 (left to right)


# joining tuples

t1 = (1,2,3)
t2 = ('a',)

t3 = t1+t2 # join using + operator
print(t3) #(1, 2, 3, 'a')


#Multiply Tuples: repeat same tuple elements
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#Tuple Methods
#Python has two built-in methods that you can use on tuples.

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

tt = ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print(tt.count("apple")) # 2

print(tt.index("cherry")) # 2: first occuring element


