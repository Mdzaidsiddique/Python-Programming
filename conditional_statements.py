# conditions: ==, !=, <, > >=, <=

a = 600
b = 500

#if
if a>b:
    print(f"a {a} is greater than b {b}") #identation is must, otherwise get error

# b = 1200
# a = 1200
# if..elif...else
if a>b:
    print(f"a {a} is greater than b {b}")
elif a<b:
    print(f"b {b} is greater than a {a}")
else:
    print("a and b are equal")


# Ternary Operators, or Conditional Expressions: concise way to perform conditional assignments
# <value_if_true> if <condition> else <value_if_false>
# sort hand if
if a>b: print("a is greater")

# sort hand if else
print("a is greater") if a>=b else print("b is grater")

print("a") if a>b else print("b") if b>a else print("both are equal")

# and : logical operator use to combine conditional statements
a = 500
b = 300
c = 200
if a>b and b>c:
    print("a is greater than b and c : both conditon are true")

# or : logical operator use to combine conditional statements
if a>b or b<c:
    print("one condition is true")

# not : logical operator used to reverse the result of conditional statements
if not a<b:
    print("a is not less than b")

# nested if: if condition inside if
x = 234
if x>100:
    print("x is greater than 100")
    if x>200:
        print("x is greater than 200")
        if x>250:
            print("x is greater than 250")
            if x==300:
                print("x is equal to 300")
            else:
                print("x is not equal")
        else:
            print("x is not reater than 250")
    else:
        print("x is not greater than 200")
else:
    print("x is less than 100")

# pass keyword: if statement can not be empty but for any reason if we dont have any content then we can use pass 
# to avoid error
if a>b:
    pass