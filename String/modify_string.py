# Python has set of built-in method that we can use to modify our string

# Upper and lower Case (upper() & lower())
str = "Welcome"
upper_str = str.upper()
lower_str = upper_str.lower()

print(str, upper_str, lower_str)

# Remove whitespces [strip() => remove leading & trailing whitespaces]
str = ' hello , , world   '
print(str)
print(str.strip())


# Replace String: [replace("s1", "s2") => method to replace string s1 with s2]
str = "Welcome Alif"
new_str = str.replace("Alif", "Mr. Zaid Alif Siddique")
print(str, " : ", new_str)

# Split String: [split(seperator) => return list with the help of seperator, default seperator is " "]
str = "jo jo the king"
list_str = str.split()
print(list_str)