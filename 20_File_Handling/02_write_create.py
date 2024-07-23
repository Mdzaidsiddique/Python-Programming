# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

f = open("20_File_Handling/demo_file.txt", "a")

f.write("\n adding more content via append mode")

f = open("20_File_Handling/demo_file.txt")
print(f.read())
f.close()

# write: overwrite
f = open("20_File_Handling/demo_file.txt", "w")
f.write("Oops! i have overwrite all the content")

f = open("20_File_Handling/demo_file.txt")
print(f.read())


# Creating new files
# "x" - Create - will create a file, returns an error if the file exist

f = open("20_File_Handling/new_demo_file.txt", "x")


