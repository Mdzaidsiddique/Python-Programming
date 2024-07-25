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
    # if isinstance(x, list):
        total+=1

print(total)


# total = sum([1 for x in l1 if isinstance(x, list)])

# sort word based on their length
words = ["abc", "d", "", "ab", "dfrsff"]
print(sorted(words))
words.sort(reverse=True)

def word_sort(word):
     return len(word)

words.sort(key = word_sort)

print(words)

# shallow copy and deep copy
o_list = [1,2,3,4]

import copy
s_list = copy.copy(o_list)
d_list = copy.deepcopy(o_list)

# generator implimentation
# 0 to 10 we need to generate
print([x for x in range(0, 11)])

def gen(n):
     for i in range(n):
          yield i

for i in gen(11):
     print(i)

# generator expression
sqr_num = (x**2 for x in range(0, 11, 2))
print(sqr_num.__next__())
print(next(sqr_num))

for i in sqr_num:
     print(i)

# generate a cubic value till n
def cube_gen(n):
     for i in range(n):
          yield i**3

cubeic_num = cube_gen(6)
for i in cubeic_num:
     print(i)


print(7/2, 7//2, 2/7, 2//7)

# dict comprehension
# create a dictionary of square of a number till n as a value , and number as a key

dict = {x: x**2 for x in range(1,11,2)}
t_dict = {key: value+1 for key, value in dict.items()}

print(dict)
print(t_dict)

print(dict[3], dict.get(0))
# print(dict.keys(), ": ", dict.values(), ": ", dict.items())

# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# print(my_dict.get('name'))
# print(my_dict['name']) 

# a variable available only inside the region it is created is called scope
built_in_scope = "reserved keywords/ len/ print etc"

global_scope = 34

if True:
     local_scope =  45

def enclosing():
     score = 45 #enclosing scope
     def en():
        return score 
     
# find total occurance of each element in a list
# 1st approach
list = [1,2,2,2,4,1,1,1,'a','a', 'c', 's']

def occurance(list, e):
     return list.count(e)

print(occurance(list, 'a'))

dict = {}
for x in list:
    if x in dict:
        dict[x] +=1
    else:
         dict[x] = 1

print(dict)

mapped = {element: list.count(element) for element in list}
print(mapped)

from collections import Counter
print(Counter(list))


# square a number of a range of list between 5 to 10
sq5_10 = [x**2 for x in range(15) if x>=5 and x<10]

# square a number between  5 to 10 an dcube below 5
sq_cube = [x**3 if x<5 else x**3 if x<10 else x+x for x in range(15) if x<=12]

print(sq_cube)

# is and ==
a = [1,2,3]
b = [1,2,3]

a==b #check content of object 
a is b #check is it referenc eto same object or not in momory

# tuple 
t = (1,2,3,1)

print(len(t), t.count(1), t, t.index(1))

# t = (1,2,3)
# l = list(t)

# l.append(4)
# l.remove(2)
# l.pop(0)
# t = tuple(l)
# print(t)


tuple1 = (1,2,[2,3],5) # we can change the list inside tuple
tuple1[2][0] = 3
tuple1[2][1] = 4
tuple1[2].append(6)
tuple1[2].pop() 
print(tuple1)

# but we can't change tuplle inside list
list1 = [1,2,(3,4)]

# convert list to dictionary
d = {i+1:list1[i] for i in range(len(list1))}
print(d)

a = ['zaid', 'umair', 'salman']

# map
def mail_creator(name):
     return name+"@gmail.com"

m = map(mail_creator, a)

for email in m:
     print(email)