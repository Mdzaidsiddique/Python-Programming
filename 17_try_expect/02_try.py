#  Try to open and write to a file that is not writable:
try:
    f = open("demo_file.txt")
    try:
        f.write("hello world")
    except:
        print("something is wrong")
    finally:
        f.close()
except:
    print("somethinf went wroing when opening the file")



# Throw(raise) an exception
x = -1
if x<0:
    raise Exception("-ve Number")

"""
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""

x = "hello"
if not type(x) is int:
    raise TypeError("only integer is allowed")