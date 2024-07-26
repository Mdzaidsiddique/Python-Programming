# find total # occurance of each iteam in a list

list = [1,2,3,2,3,4,5,5,5,8]

def count(list, i):
    return list.count(i)

# print(count(list, 5))

# using dictionary
def map_list(list):
    result = {}
    
    for i in list:
        if i in result:
            result[i] +=1
        else:
            result[i] = 1
    return result

print(map_list(list))

# using counter from collection module
from collections import Counter

print(Counter(list))

# using dictionary comprehension
occurance = {element:list.count(element) for element in list}
print(occurance)

# find the sum of all element
def find_sum(list):
    return sum([x for x in list])

# find product
def find_product(list):
    product = 1
    for x in list:
        product*=x
    return product

# reverse list in place
def reverse_list(nums):
    nums.reverse() #reverse inplace
    # return nums[::-1] 

# check if list is empty
def is_empty(list):
    return len(list)==0

# find the index of first occurance of each element of a list
def occurance_of_each_element_index(list):
    return {element: list.index(element) for element in list}

# create new list containing only ecen number form existing list
def only_even(list):
    return [x for x in list if x%2==0]

# create a new list with the square of each element of a list
def square_list(list):
    return [x**2 for x in list]

# sort list in ascending and descending order
def sort_list(list):
    # return sorted(list)
    list.sort(reverse = True)

# sort list with custom logic
def custom_sorting_logic(element):
    return abs(50-element)

l1 = [50,34,23,67,1,2,-48,-49,-56]

l1.sort(key=custom_sorting_logic)

# check all elements are positive
def check_positive(list):
    return all(x>0 for x in list)

# find second largest element in a list
def second_largest(nums):
    return sorted(nums)[-2]

# remove all the occurance element of a specific element 
def remove_occurance(nums, target):
    return [x for x in list if x is not target]

# find common element between two list
def find_common(l1, l2):
    return [x for x in l1 if x in l2]
    # return list(set(l1) & set(l2))

# check if the list is palindrome
def check_plaindrome(nums):
    return nums == nums[::-1]

# flatten a list of lists in a single list
def flatten_lists(lists):
    return [item for sublist in lists for item in sublist]
    # return sum(lists, [])

# remove 1st and last element
def remove_first_last(list):
    return list[1:-1]

# find the last occurance of a element in a list
def find_last_occurance(list, target):
    return abs(len(list)-1 - list[::-1].index(target))

# rotate a list to left by given number of position
list = [1,2,3,4,5,6]
def rotate_left(list, pos):
    pos %= len(list)
    return list[pos:] + list[:pos]

print(rotate_left(list, 3))