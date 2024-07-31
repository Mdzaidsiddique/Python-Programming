# zip : built in functions that take two or more iterable and return iterable of tuples

l1 = ['a', 'b', 'c']
l2 = [1,2,3]

zipped = zip(l1,l2)
# for i in zipped: print(i) # (a,1),(b,2),(c,3)
print(zipped.__next__())


# unzip

zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]
l1, l2 = zip(*zipped_list)

print(l1, l2)