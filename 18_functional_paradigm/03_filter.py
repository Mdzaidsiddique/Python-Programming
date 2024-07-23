# The filter() method filters the given sequence with the help of a function 
# that tests each element in the sequence to be true or not. 

def is_even(n):
    return n%2 == 0

# Define a list of numbers
numbers = list(range(0,20))

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)

print(type(even_numbers)) #<class 'filter'>
print(list(even_numbers))
