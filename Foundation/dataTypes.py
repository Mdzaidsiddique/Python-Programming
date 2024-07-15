# Data Types : Python dont have data types but the value asssign to a variable or stored to a variable have data types
# a = 10 then 10 has int type not a
"""
Built-in Data Types
- In programming, data type is an important concept.

- Variables can store data of different types, and different types can do different things.

- Python has the following data types built-in by default, in these categories:
"""

"""
- Text Type     :   str
- Numeric Types :	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type  :	dict
- Set Types     :	set, frozenset
- Boolean Type  :	bool
- Binary Types  :	bytes, bytearray, memoryview
- None Type     :	NoneType
"""

# We can get the data type of any object by using the type() function:

# Text Type :: str
x = "string" #str
print(x, type(x))

# Numeric Types :: int, float, complex
x = 10;   #int
x = 10.0  #float
x = 1j    #complex

# Sequence Types :: list, tuple, range
fruits_list = ["apple", "Banana", "Orange"]  #list
fruits_tuple = ("Apple", "Banana", "Orange") #tuple
x = range(6) #range
print(x, x[1])

# Mapping Type :: dict
student = {
    "name":"Alif",
    "Roll":10}
print(student)

# Set Types :: set, frozenset
fruits_set = {"apple", "banana", "orange"} #set
fruits_fs = frozenset({"apple", "banana", "orange"}) #frozenset
print(fruits_set, fruits_fs)

# Boolean Type :: bool (True, False)
x = True 
y = False
print(x, y)

# Binary Types :: bytes, bytearray, memoryview
x_bytes = b"Hello" #bytes
x_bytearray = bytearray(5); #bytearray
x_memoryview = memoryview(bytes(5)) #memoryview

print(x_bytes, x_bytearray, x_memoryview)

# None Type :: NoneType
x_none = None 
print(x_none)


## Setting the Specific Data Type
x = str("Hello World")
x = int(10)
x = float(10.20)
x = complex(10J)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="Zaid", age=26)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
print(x)



