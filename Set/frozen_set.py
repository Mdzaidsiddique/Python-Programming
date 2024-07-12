# set can contain only hashable (immutable) elements so, we can't define set inside snother set
# *Set items are unchangeable, but we can remove items and add new items

# Frozenset: A frozenset is an immutable version of a set (hashable)
# Set: Mutable. You can add, remove, and modify elements in a set.
# Frozenset: Immutable. Once created, you cannot change its elements.

fzs1 = frozenset([1,3,4])
fzs2 = frozenset([5,6,7])

print(fzs1, type(fzs1)) #frozenset({1, 3, 4}) <class 'frozenset'>

super_fzset = {fzs1, fzs2}

print(super_fzset, type(super_fzset)) #{frozenset({5, 6, 7}), frozenset({1, 3, 4})} <class 'set'>

# Creating a frozenset
fs = frozenset([1, 2, 3, 4])

# Attempting to modify the frozenset will result in an error
# fs.add(5)  # This will raise an AttributeError

# Set operations with frozensets
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# Union
union_fs = fs1.union(fs2)
print("Union:", union_fs)  # frozenset({1, 2, 3, 4, 5})

# Intersection
intersection_fs = fs1.intersection(fs2)
print("Intersection:", intersection_fs)  # frozenset({3})

# Difference
difference_fs = fs1.difference(fs2)
print("Difference:", difference_fs)  # frozenset({1, 2})

# Symmetric Difference
symmetric_difference_fs = fs1.symmetric_difference(fs2)
print("Symmetric Difference:", symmetric_difference_fs)  # frozenset({1, 2, 4, 5})
