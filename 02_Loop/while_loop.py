# python has two primitive loop commands (while and for loop)

# while loop: execute set of statements as log condition is true
i=0
while(i<6):
    print(i)
    i=i+1 # remember increment otherwise it will become infinite loop

# break statement: terminate the loop

i =1
while(i<6):
    print(i)
    # i=i+1
    if i==3:
        print(i, " is equal to 3")
        break
    i=i+1

# continue statement: skip the iteration (continue to next iteration if condition satisfied)
i=0
while i<7:
    i=i+1
    if i==4:
        continue
    print(i)

# the else statements: with the else condition we can run the block of code once the condition no longer true
i = 0
while i<6:
    print(i)
    i += 1
else:
    print("The loop is over, i is no longer less than 6")