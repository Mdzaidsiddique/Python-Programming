# {'expressions' for key, value in 'iterables' (if condition)}

num_dict = {x*2 for x in range(1,11)}

print(num_dict)

dict_comp = {x*2 for x in range(1,11) if x%2==0}
print(dict_comp)

# transforming existing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_dict = {k:v**2 for k,v in original_dict.items()}

print(transformed_dict)


squared_num = {x:x**2 for x in range(1,11)}

print(squared_num)
squared_num.clear()


keys = ["Python", "Java", "c++"]
default_value = "powerful Language"

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)


person = {"zaid": 24,
          "amir" : 26,
          "ahsan": 23}

# add age by 1 year of everyone
new_person = {name: age + 1 for name, age in person.items()}
print(new_person)