# To delete a file, you must import the OS module, and run its os.remove() function:

import os

os.remove("20_File_Handling/new_demo_file.txt")


# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os
if os.path.exists("20_File_Handling/new_demo_file.txt"):
    os.remove("20_File_Handling/new_demo_file.txt")
else:
    print("File does not exist")


# To delete an entire folder, use the os.rmdir() method:
# os.rmdir("folderName")