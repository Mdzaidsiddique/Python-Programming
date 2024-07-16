# Random Number: Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

import random;

# Random float: 0.0 <= x < 1.0
print(random.random())

# random integer: 1 <= x <= 6
print(random.randint(1,6))

# random integer: 1 <= x < 10
print(random.randrange(1,10))

print(random.randrange(1,10,2))

choices = ['apple', 'banana', 'cherry', 'date']

# singale random choice
print(random.choice(choices))

# multiple random choices with replacement
print(random.choices(choices, k=3)) 

# multiple  random choices without replacement
print(random.sample(choices, 3))

# suffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)