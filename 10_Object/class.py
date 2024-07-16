# python support oop pradignms as well
# everything in python are object (properties and methods)

# class: blueprint for creating object

class myclass:
    name = "zaid alif"

classOne = myclass()

print(classOne)
print(classOne.name)

# __init__()
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# __init__() set up the initial state of an obj by assigning value to it

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("zaid alif", 25)

print(person1.name, ":", person1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# __str__() function: set the string representation of object
class gentlePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} year old"
    
gentleman = gentlePerson("zaid", 45)

print(gentleman)