num_dict = {x*2 for x in range(1,11)}

print(num_dict)

dict_comp = {x*2 for x in range(1,11) if x%2==0}
print(dict_comp)

# transforming existing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_dict = {k:v**2 for k,v in original_dict.items()}

print(transformed_dict)