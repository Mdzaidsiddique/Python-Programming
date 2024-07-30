# enumerate(Iterable, start=0(default))

# built in method that allow to iterate over any iterable and have automatic counter


tuple = (1,2,3,4,5)

for index, element in enumerate(tuple, start=1):
    print(index, element)