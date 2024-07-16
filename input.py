# Python allow user input
# Python stops executing when it comes to the input() function, and continues when the user has given some input.
# in python 2.7: raw_input()
# in python 3.6: input()

username = input("Enter username..") 

print(f"You have entered username : {username}")

# everytime we get value from user input is comes in string type


score = int(input("Enter your Score :\n")) #\n for new line

if score>=100:
    print("please enter score less then 100")
    exit()
elif score<0:
    print("Score should be +ve")
    exit()
else:
    print(f"Your score is : {score}")


