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
occurance = {element: list.count(element) for element in list}
print(occurance)

