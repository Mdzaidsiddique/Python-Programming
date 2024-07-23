import functools
num = [1,2,3,4,5]

# Use reduce to compute the product of list elements
num_product = functools.reduce(lambda x,y : x*y, num)

print(num_product)