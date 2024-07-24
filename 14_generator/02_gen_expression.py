# generator expression :: shorter way to write generator function, also called anonymous generator
squared_num = (x**2 for x in range(1, 10))

print(squared_num.__next__())
print(squared_num.__next__())

for i in squared_num:
    print(i)