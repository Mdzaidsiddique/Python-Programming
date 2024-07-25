tup = (1, 2, 3, 4, 5)

# find length
def tuple_length(tup):
    return len(tup)

# concatinate two tuple
def concat_tuple(t1, t2):
    return t1+t2

# access elements in a tuple
def access_tuple(tup):
    for x in range(len(tup)):
        print(tup[x])

# count occurance of element in tuple
def count_occurance(tup, element):
    return tup.count(element)
    
# check if an element exist in tuple
def is_exist(tup, element):
    return element in tup

# convert tuple in string
def tuple_to_string(tuple):
    return str(tuple)

# find the index of an element in a tuple
def find_index(tup, element):
    return tup.index(element)

# convert list to tuple
def list_to_tuple(list):
    return tuple(list)

# iterate through tuple using for loop
for i in range(len(tup)):
    print(tup[i])

# iterate through tuple using while loop
i = 0
while i < len(tup):
    print(tup[i])
    i+=1

# find max and min element in tuple
def max_min_tuple(tup):
    return f"maxximum is {max(tup)}, and minimum is {min(tup)}"

print(max_min_tuple(tup))

# convert tuple of string to a single string
def tup_to_single_string(tup):
    return ", ".join(tup)

# remove an element from tuple
def remove_from_tuple(tup, element):
    return tuple(x for x in tup if x != element)

# find the common element between two tuple
def common_in_tuple(t1, t2):
    return list(x for x in t1 if x in t2)

# sort tuple of integers in ascending order
def sort_int_tuple(tup):
    return tuple(sorted(tup))

# sort tuple of integers in descending order
def sort_int_tuple_desc(tup):
    return tuple(sorted(tup, reverse=True))

# find the sum of elements in tuple
def find_sum(t1):
    return sum(t1)

# merge two tuple and remove duplicate
def merge_and_remove_duplicates(t1, t2):
    return tuple(set(t1).union(set(t2)))

# find the first and last element of tuple
def find_first_and_last(tup):
    return tup[0], tup[len(tup)-1], tup[-1]

# reverse the tuple
def reverse(tup):
    return tup[::-1]

# convert int tuple to string tuple
def int_tuple_to_str_tuple(tup):
    return tuple(str(x) for x in tup)

# count number of even and odd number in a tuple
def count_even_odd(tup):
    even = sum(1 for x in tup if x%2==0)
    # odd = sum(1 for x in tup if x%2!=0)
    odd = len(tup)-even
    return even, odd

# find the product of all element in a tuple
def find_product(tuple):
    product = 1
    for i in range(len(tuple)):
        product *= tuple[i]
    return product

# split tuple in equal parts
def split_tuple(tup, no_of_parts):
    avg = len(tup)//no_of_parts
    return tuple([tup[i:i+avg] for i in range(0, len(tup), avg)])

# find the frequency of each element of a tuple
def find_frequency(tuple):
    return {x:tuple.count(x) for x in tuple}

# find th edifference between two tuple
def find_difference(t1, t2):
    # return tuple(set(t1).difference((t2)))
    return tuple([x for x in t1 if x not in t2])

# check if a tuple is subset od another tuple
def is_subset(sub, tuple):
    return all(x in tuple for x in sub)

print(is_subset((2,4,6),(1,2,3,4,5,6,7,8,9)))