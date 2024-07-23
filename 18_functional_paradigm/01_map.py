# The map () function returns a map object(which is an iterator) of the results after 
# applying the given function to each item of a given iterable (list, tuple, etc.).

def double(n):
    return n**2

numbers = [1,2,3,4,5]
double_numbers = map(double, numbers)

result = list(double_numbers)
print(result)
print(numbers, '\n', tuple(result))


def add_Mr(name):
    return "Mr. "+name

names = ["zaid", "kaif", "umair"]
updated_names = map(add_Mr, names)

print(list(updated_names), type(updated_names)) #map type