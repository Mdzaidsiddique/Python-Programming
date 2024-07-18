# write a function that generate even number upto specified number

def even_generator(target):
    for even_num in range(2, target, 2):
        # return even_num #this will return single value 2, and after that execution will terminate coz of return kw
        yield even_num

# we can talke a list and and append every time even_num in list and at last return list, but that will return list
# but we want every time number not list

for i in even_generator(10):
    print(i)


# yield: return a value and also keep track in memory at what value it is previousaly

"""
The yield keyword in Python is used to define a generator, which is a special type of iterator. 
Generators allow you to iterate over a sequence of values without creating the entire sequence in memory at once. 
Instead, they generate values one at a time and yield them to the caller,
pausing the function's state until the next value is requested

 This makes generators memory-efficient
"""