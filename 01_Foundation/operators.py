# Operators: are used to perform operation bw values and variables
# operand1 operator operand2

"""
Python divides the operators in the following groups:

1- Arithmetic operators
2- Assignment operators
3- Comparison operators
4- Logical operators
5- Identity operators
6- Membership operators
7- Bitwise operators
"""

# 1- Arithmetic operators: (+,-,*,**,%,/, // -> floor division)
num1 = 100
num2 = 40
print(num1+num2)
print(num2-num1)
print(num1/num2)
print(num1*num2)
print(num1**2)
print(num1//3)
print(num1%6)

# 2- Assignment operators: (=, +=, =+, -=, =-, )
x = 5
x += 5 # x = x+5
x -= 5 # x = x-5
x *= 5 # x = x*5
x /= 5 # x = x/5
# //=, %=, **= 

# x &= 5 # x = x&5
# x |= 5 # x = x|5
# x ^= 5 # x = x^5
# x >>=5 # x = x>>5

print(x:=3) # x = 3 then print(x)

# 3- Comparison operators: used to compare two value (==, !=, >, <, >=, <=)
    # and: Returns True if both statements are true 
    # or : Returns True if one of the statements is true
    # not: Reverse the result, returns False if the result is true
print(4>2 and 5<3)
print(3==3 or 3>4)
print(not(3>2 and 5>2))

# 5- Identity operators (is, is not) 
x = 5
y = x
print(x is y) #return true is both are same
print(x is not y) # returns true if both are not the same object

# 6- Membership Operator(in, not in): Membership operators are used to test if a sequence is presented in an object
    # in: true if specefied value present inside object
    # not in: opposite of in
print("z" in "zaid")

# 7- Bitwise operator: used to compare binary numbers
# (&, |, ^, ~, <<, >>)

# reference: https://www.w3schools.com/python/trypython.asp?filename=demo_oper_and