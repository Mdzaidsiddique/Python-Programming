# write a function to square a number

def square(number):
    print("square is:", number**2)

square(4) # square is: 16

result = square(4)
print(result) # None, because we havent return any value we just printed


def square(number):
    return (number**2)

square(4) # Nothing

result = square(4)
print("Result is:" , result) #Result is: 16