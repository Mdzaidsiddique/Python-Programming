list = ["orange", "mango", "kiwi", "pineapple", "banana"]

list.sort() # sort in asscending prder
print(list)

list = [100, 50, 65, 82, 23]
list.sort()
print(list)

list.sort(reverse=True) #to sort in descending order sort(reverse=True)
print(list)

# customized sort : sort(key = my_func)
# Sort the list based on how close the number is to 50: (less then or greater)
num = [100, 240, 70, 40, 56]
def fifty_sort(n):
    return abs(n-50)

num.sort(key=fifty_sort)

print(num)

# case insensitive sort(key = str.lower)
list = ["Apple", "apple","Orange", "Mango", "kiwI", "pineapple", "banana"]
list.sort() # case sensitive sort
print(list)
list.sort(key = str.lower) #case in-sensitive

print(list)

num = [100, 240, 70, 40, 56]
num.sort() #sort in ascending order
print(num)
num.reverse() # reverse
print(num)