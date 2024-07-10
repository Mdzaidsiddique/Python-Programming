# in python we can not combine number and string with +
age = 34
name = 'zaid'

# name_and_age = name+age  # TypeError: can only concatenate str (not "int") to str

# But we can combine strings and numbers by using f-strings or the format() method!

# F-string (introduces in python 3.6): preffered way
'''To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.'''

name_and_age = f"{name} and {age}"
name_and_age = f"my name is {name} and i am {age} year old"

print(name_and_age)

#Placeholder & Modifier(:.2f etc) => placeholder {} to contain variable/operation/function and modifire to modify the value
# Modifi: =>

graduation_percentage = 88
short_intro = f"Hi i am {name} and i am {age} year old, and i got {graduation_percentage:.2f} in my graduation"

print(short_intro)

# perform math operation in placeholder
score = 15
print(f"new score {score * 5}")
print(f"new score {score * 5 :.2f}")