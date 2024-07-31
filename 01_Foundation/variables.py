# Variables Name

"""
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.
"""

first_name = "zaid"
firstName = "zaid"
_firstName = "zaid"
_first_name = "zaid"
first_name2 = "md"

# Assigning Multiple Variables

## many value to multiple variable
x,y,z = 1,2,3

## one value to multiple variable
a=b=c=45

print(b)

# Unpack :: Extracting the value from collection into variables
students = ["salman", "zaid", "amir", "umair"]

salman, zaid, amir, umair = students

print(salman, umair)

# print(5+"five") # error :: we can't use + with num and string at same time


""" 
Global Variables 
:: variables created outside a function is known as GV
:: it can be used by everyone, both inside of functions and outside.
"""

x = 'awesome'; # Global Variable

def myfunc():
	print("Python is "+x) 

myfunc()

"""
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
"""

x = "awesome"
def func():
	x = "fantastic"
	print("python is ", x)

func()

print("Python is "+ x)

""" 
Global Kwyword :: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""
def funcOne():
	global x
	x = "Easy to learn"

print("Python is "+x)
funcOne()
print("Python is ", x)

# also we can use global keyword to cahnge the global variable inside a function

score = 10

def funTwo():
	global score
	score = 90
	print("Score inside fun is ", score); # 90

funTwo()
print("Score outside fun is ", score) # 90