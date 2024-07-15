# functions are set of instruction to perform certain task
# it executes only when it called
# we dyfine function with def keyword

def addition(x, y): # x,y: parameter
    return x+y

# at time of calling function #args should be equal to #parameter otherwise get error
result = addition(5,7) #5,7: args or argument
print(result)

def greet(name):
    return f"Hello there, Greetings from Mr. {name}"

print(greet("alif"))

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# if #parameter is unknown : add * before args : function recieve a tuple
def language_known(*languages):
    for lang in languages:
        print(lang)

language_known("Java", "Python", "JS", "HTML", "SQL")

my_lang = list(("Java", "Python", "JS", "HTML", "SQL"))
print(my_lang, type(my_lang))
language_known(my_lang) 

# Keyword arguments:
def lang(lang1, lang2, lang3):
    print("Latest leared language is :",lang3)

lang(lang1 = "JS", lang2 = "Java", lang3 = "Python")

# arbitrary keyword **args: #k-arg are unknown : function recieve as dict
def child(**kids):
    print("Last name is :", kids["lname"])

child(fname = "zaid", lname = "alif")


# default parameter value: if we call without args then fn will take default value
def nationality(country = "India"):
    print("I am from :", country)

nationality()
nationality("USA")

# we can pass any data types(list, tuple, set, dict, etc) in function and it will be treated as same dt inside fn


# return: reserved keyword to let a fn return value
def addition(num1, num2):
    return num1+num2

result = addition(5,6)
print(result)

# pass: fn block can't be empty, we can use pass keyword to avoid getting error
def empty_func():
    pass

# keyword args: x=3, y=5, etc
# positional args: 3,5, etc

# positional-only args: args, /
def myfunc(a,/):
    print(a)

myfunc(5)
# myfunc(x=5): error: unexpected keyword argument 'x'

# keyword-only args: *, args
def func(*, x):
    print(x)

func(x=109)
# func(108) : error: func() takes 0 positional arguments but 1 was given

# positional and keyword args: we can combine both
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only

def my_function(a,b,/,*,c,d):
    print(a,b,c,d)

my_function(1,2,c=3,d=4)

# recursion: function which call itself
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1) 

n = 5
print(f"factorial of {n} is {factorial(n)}")
