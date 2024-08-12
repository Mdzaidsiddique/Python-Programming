username = "zaid"
""
print(username)

# please refer .txt file for commands

f = open("dummy.py")
f.__next__() # this will throw exception after reading last line (file end)
f.readline() # this will return '' after reading last line(file end)
f.readlines() # this will read all lines and return list of all line comma seperated

f.close()