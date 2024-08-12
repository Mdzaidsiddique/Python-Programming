# Decorator: A decorator is a higher-order function that takes another function as an argument, adds some functionality, 
# and returns a new function. It allows modifying or extending behavior of functions or methods.

# A wrapper is the inner function defined within a decorator that actually performs the added functionality.
# A decorator is the outer function that takes a function as an argument, defines a wrapper function to modify it, and returns the wrapper.

# Decorators are used to modify the behavior of functions or methods. Use them when you want to add functionality 
# like logging, caching, or authentication to existing functions without modifying their source code. 
# They help in separating concerns and improving code readability.

# timer decorator 

import time
def timer(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        time.sleep(args[0])
        func(*args)
        end_time = time.time()
        print(f"{func.__name__} has taken {start_time-end_time} sec of time")

    return wrapper

@timer
def calculate_fn_exe_time(n):
    print(f"execute this function after {n} sec")

calculate_fn_exe_time(3)




# another decorators 
def dec_fun(functionp):
    def wrapper(*args):
        
        print(*args)
        functionp(*args)
        print('after execution')

    return wrapper

@dec_fun
def myfun(name, age):
    return name, age

myfun("zaid", 45)