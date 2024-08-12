# String: Set of characters, surrounded by '', "" or """ """"
# Immutable (Can't change)
# strings in Python are arrays of bytes representing unicode characters.

string_1 = "Marhaban bil-'alam"

print(string_1)


# Multiline string :: can assign multiline string with three double or single quotes
about_me = """A highly motivated individual with a strong interest in the field of 
Software Development with good presentation and interpersonal skills & Strong analytical capabilities,
looking to work in learning environment along with utilising my skills and knowledge to the fullest."""

# print(about_me)

str = "Zindagi aa raha hun mai"

# Accessing Characters from String
print(str[0])

# Looping through string
for c in str:
    print(c)

for character in "Loveable":
    print(character)

# String length
print(len(str))

# Check String (in) :: to check certain characters are present inside string or not
print("nd" in str)  # in: true/false

if('Zindagi' in str):
    print("Aa raha hun mai..")

# not in :: -ve of in (true if certain phrase or characters are not present in string)

txt = "Python is beautiful"
if("not" not in txt):
    print("Python is beautiful")

# string concatination (+): [combine two string]
first_name = "zaid"
middle_name = "alif"
last_name = "siddique"

full_name = first_name+" "+middle_name+" "+last_name

print(full_name)

s = """
heu
my 
name"""
print(s, type(s))


# reversed string in python
s = "zaid"
reversed_s = s[::-1]



# str(): Simplified and readable.
# repr(): Detailed and unambiguous.
import datetime

now = datetime.datetime.now()

print(str(now))   # Output: 2024-07-24 12:34:56.789123
print(repr(now))  # Output: datetime.datetime(2024, 7, 24, 12, 34, 56, 789123)
# str() for a user-friendly representation and repr() for a detailed, unambiguous representation.


# string path conversion
path = "C:\Users\mdzaids\Desktop\folder_name\homepage.png"
# by using double backslash
path = "C:\\Users\\mdzaids\\Desktop\\folder_name\\homepage.png"

# by using raw string 
path = r"C:\\Users\\mdzaids\\Desktop\\folder_name\\homepage.png"
