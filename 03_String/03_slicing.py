# slice [start:end] return range of characters by using slice
# start(inclusive) & end(exclusive)

str = "my name is khan"

name = str[3:8] 
print(name)

# slice from the start [:end] : from start till specefied index(exclusive)
slice_from_start = str[:15] # my name is khan
my_name = str[:8] # my name

# slice to the end [start: to the end] : from specified index till end
print(str[2:]) #name is khan

# Negative indexing :: Use negative indexes to start the slice from the end of the string:
print(str[-1]) #n

strr = "Hello World!"

print(strr[-6:-1]) # World