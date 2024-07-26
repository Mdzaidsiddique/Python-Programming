# lambda: small annonymous function 

# syntax:
# lambda arguments : expression 

add10 = lambda a: a+10 
print(add10(5))

# can take mulitple agrs but only one expression
multiply = lambda num1, num2, num3: num1*num2*num3
result = multiply(2,3,4)

print(result)

# lambda function inside normal function

def power(n):
    return lambda a: a**n

power2 = power(2) # return a function
print(power2(6)) # 36

power3  =power(3)
print(power3(5)) #125
