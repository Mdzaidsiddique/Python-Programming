"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# when an error occured, or exception raised, python will stop execution and generate error message
# thease exceptions can be handled using try statement

# x = 2/0 #ZeroDivisionError: division by zero
try:
    x = 2/0
except:
    print("any number cannot be devided with zero")

# many exception
try:
    print(z)
except NameError:
    print("z is not defined")
except:
    print("something wrong happpens")


# else: You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("hello")
except:
    print("somethinf went wrong")
else:
    print("everything is fine")

#Finally: The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(z)
except:
    print("z is not defined")
finally:                                    #This can be useful to close objects and clean up resources:
    print("the try-except block is finished")

