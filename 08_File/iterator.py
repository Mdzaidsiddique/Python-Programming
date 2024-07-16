# for line in open("file_reading.py"):
#     print(line)


# with while loop 
f = open("file_reading.py")
while True:
    line = f.readline()
    if not line: break
    print(line, end="")