# Polymorphism in function: one function multiple uses

def multiply(input1, input2):
    return input1*input2

# output = multiply(2, 5)
output = multiply(2, "zaid") # zaidzaid
output = multiply("alif", 3) #alifalifalif

print("Output is :", output)