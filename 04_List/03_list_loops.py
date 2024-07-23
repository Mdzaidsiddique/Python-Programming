# For loop
list = ['apple', 'blackcurrant', 'watermelon', 'cherry']

# looping through values
for element in list:
    print(element)

# looping through index
for i in range(len(list)):
    print(i, list[i])

# While loop
i=0
while(i<len(list)):
    print(list[i])
    i = i+1 # i++ will not work

# list comprehension
thisList = [1,2,3,4,5,6,7,8,9]
[print(x) for x in thisList]
