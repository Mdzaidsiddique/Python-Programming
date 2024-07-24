#  dict comprehension
#  shallow and deep copy
lsit = ([1,2],4,5) # we can change list inside tuple but not tuple inside list
lsit[0][1] = 3
# print(lsit)

a=[1,2,3,4,5,6,7,8,9]
 #=10,20,30,40,50,60
print(a[::2]) #[1, 3, 5, 7, 9]
print(a[::])  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[::-2]) # -ve: reverse list, -2 is step

# [start, end, step]

# find the first element of each inner list
l1 = [[1,2,3],100, [4,5,6], [7,8,9]]
print([x[0] for x in l1 if isinstance(x, list)])

# .format()

txt = "hey i am {} from {}"
welcome_text = txt.format("zaid", "India")

print(welcome_text)

# *args and **kwargs
def temp(*args): #tuple
    print(args, type(args))
 
temp(1,2,3,"zaid")

def temp2(**kwargs): #dict
    print(kwargs, type(kwargs))

temp2(name = "zaid", password = "alif123")

# map in python
# map : it will process over each elemetns of iterable and provie map object(iterable)
num = [2,3,4,5,6]

def multiple_by_two(num):
    return num*2

result = map(multiple_by_two, num)
print([x for x in result])

# convert list to dictionary
list = [1,2,3,4,5,6]

# 1st approach
keys = len(list)

dict = {}
for i in range(keys):
    dict[i+1] = list[i]

print(dict)

class Zaid:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

zaid = Zaid("zaid alif", 34)
print(str(zaid))
print(repr(zaid))

# count the number of inner list
l1 = [[1,2,3], [4,5,6], 7, [8,9]]
# total_inner_list = sum([x[0] for x in l1 if isinstance(x, list)])
total = 0
for x in l1:
    if isinstance(x, list):
        total+=1

print(total)