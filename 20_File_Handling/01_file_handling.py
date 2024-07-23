# key fn for working in file is open(file_name, mode(optional))

# 4 different mode:
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - text mode (default)

"b" - binary mode
"""

f = open("20_File_Handling/demo_file.txt") #same as open(file, rt) r-read, t-text

# print(f.read())

f.read(6) #return 6 first character

# readline()
f.readline()

f.readlines()

# loop through file line by line
f = open("20_File_Handling/demo_file.txt", "r") 
for line in f:
    print(line)


# close file
f.close()