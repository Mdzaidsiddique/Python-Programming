# decorators are like tolls , we can pass any function from it
# it accepts function as parameter, return wrapper function definition

# write a decorator debug and print name of the function ehich executes and all arguments
def debug(func):
    def wrapper(*args, **kwargs):

        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k,v in kwargs.items())

        print(f"function calling {func.__name__} with {args_value} and {kwargs_value}")

        return func(*args, **kwargs)

    return wrapper


@debug
def say_hello(name):
    return f"Hello {name}"

@debug
def greet(name, greeting = "Hi.."):
    return f"{greeting}, from {name}"

print(say_hello("zaid"))
print(greet("alif", greeting="Good morning"))