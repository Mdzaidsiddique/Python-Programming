# A closure in Python is a nested function that remembers and can access variables from its enclosing scope 
# even after the outer function has finished executing.

def outer_func(msg):
    message = msg

    def inner_func(): # this fun is called closure, which is having the access of enclosing scope variables
        print(message)
        
    return inner_func

closure_exp = outer_func("Hello Mr..")

closure_exp()

# inner_func is a closure that captures the variable message from its enclosing scope (outer_func). 
# Even after outer_function has finished executing, inner_function still has access to message.
