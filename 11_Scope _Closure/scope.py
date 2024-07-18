# scope: a variable available only inside the region it is created.

# function scope: local 
def func():
    x = "x"
    return x

a = 10 #this is the global block

if 5>3: #this is the local block
    global x #way to define global variable inside local invironemnt
    x = 30
    pass

# whatever we kept inside function will only execute and assign once we called the function


# The nonlocal keyword is used to work with variables inside nested functions.
# If you use the nonlocal keyword, the variable will belong to the outer function:
# The nonlocal keyword makes the variable belong to the outer function.


# closure: every local scope kept reference of his parent score, this is called closure
