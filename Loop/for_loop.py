# for loop: used for iterating over sequence (string, list, tuple, set, dictionary)

for c in "string":
    print(c)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) # by default end='\n' in print() method, we can change it
    print(x, end="-")

print("---seperator---")

# for loop with break
for x in fruits:
    if x == "banana":
        break
    print(x)

print("---seperator---")

# for loop with continue
for x in fruits:
    if x=="banana":
        continue
    print(x)

# range() function: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1
# range(n): 0 to n-1

for i in range(6):
    print(i) #0 to 5

# range(start(inclusive), end(exclusive))
for i in range(2,10):
    print(i) # 2 to 9

# range(start, end, step): start(include), end(exclude), step(increment)
for i in range(3,100,10):
    print(i) # 3 to 100 incremented by 10

# else in for loop: 
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for i in range(5):
    print(i)
else:
    print(i, "range is over") #i=4

print(i) #4

# Note: The else block will NOT be executed if the loop is stopped by a break statement, but execute with continue
for i in range(5):
    print(i)
    if i==3: break
else:
    print("loop is over") # won't execute coz of break


# Nested loops
number = [1,2,3,4,5]
multiple = list(range(1,11))

for x in number:
    print(f"table of {x}")
    for y in multiple:
        print(f"{x} {y}'s are :",x*y)
    
