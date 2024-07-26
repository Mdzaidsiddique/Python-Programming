list = [1,2,3,4,5]

iter1 = iter(list)

print(iter1.__next__())
print(next(iter1))


# for line in open("file_reading.py"):
#     print(line)


# with while loop 
f = open("file_reading.py")
while True:
    line = f.readline()
    if not line: break
    print(line, end="")