# Python has a set of built-in methods that we can use on strings.

name = "zaid alif siddique"
first_name = "Zaid ALif"
last_name = "Siddique"

# capitalize() => Converts the first character to upper case
print(name.capitalize())

# casefold() => Converts string into lower case
print(first_name.casefold())

# title() => Converts the first character of each word to upper case
print(first_name.title())

# upper() => Converts a string into upper case
print(name.upper())

# lower() => Converts a string into lower case
print(first_name.lower())

# center(length, character) => Returns a centered string
# length => required length of the returned string
# character => Optional. The character to fill the missing space on each side. Default is " " (space)
print(last_name.center(20)) 

# count() => Returns the number of times a specified value occurs in a string
print("aliff".count('f')) #2

# find() => Searches the string for a specified value and returns the position of where it was found
print("zaid".find('i')) #2

# istitle() => Returns True if the string follows the rules of a title
print("Zaid Alif Siddique".istitle()) #True

# isupper() => Returns True if all characters in the string are upper case
print("ZAID".isupper()) #True

# islower() => Returns True if all characters in the string are lower case
print("zaid".islower()) #True

'''
Method	        Description


encode()    	Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string

format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()   	Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier

isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces

join()	        Joins the elements of an iterable to the end of the string
ljust()     	Returns a left justified version of the string
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()     	Returns a trimmed version of the string
swapcase()  	Swaps cases, lower case becomes upper case and vice versa
translate() 	Returns a translated string

'''

# zfill()     	Fills the string with a specified number of 0 values at the beginning
print("56".zfill(5)) #00056
print("45".zfill(10))



