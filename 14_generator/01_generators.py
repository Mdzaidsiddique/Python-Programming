# it generates the value with the help of yield, instead of return

"""
a function that returns an iterable in Python and uses the yield keyword is called a generator.

Generators are a special kind of iterator that allows you to iterate over a sequence of values, 
but unlike lists or tuples, they do not store the entire sequence in memory. 
Instead, they generate each value on-the-fly, which makes them memory efficient, especially for large datasets or infinite sequences.
"""

def generator_function(num):
    for x in range(2,num,2):
        yield x
    
even_gen = (generator_function(12))

for i in even_gen:
    print(i)

"""
The difference between yield and return is that yield returns a value and pauses the execution 
while maintaining the internal states, 
whereas the return statement returns a value and terminates the execution of the function.
"""

def my_gen():
    print("two")
    yield 2

    print("three")
    yield 3

gen_iterator = my_gen() # return iterable object

print(gen_iterator.__next__())
print(next(gen_iterator))
# print(next(gen_iterator)) #StopIteration



