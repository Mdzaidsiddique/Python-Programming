# Booleans represent one of two values: True or False.

# Falsy values in python: None, 0, "", False, [], {}, () (i.e empty string, list, tuple, set, dictionary)
# Truthy Values: except falsy values everything is truthy value

print(2<5) #True
print(0!=0) #False

# bool() => evaluate any value and return True or False
print(bool("Hello")) #True
print(bool(13)) #True
print(bool(0)) #False
print(bool(None)) #False
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False, and that is if you have an object 
that is made from a class with a __len__ function that returns 0 or False
"""
class my_class():
    def __len__(self):
        return 0
    
my_obj = my_class()
print(bool(my_obj)) #False

# Functions can also return boolean value, there are many inbuilt functions in python that returns boolean like ininstance()