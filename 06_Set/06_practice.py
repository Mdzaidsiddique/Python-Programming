# creating set
set1 = set() # empty set
set2 = {1,}  # non-empty set
set3 = {"apple", "banana", "cherry"}

# find length of a set
def find_length(s):
    return len(s)

# add element to a set
def add_element(s, element):
    s.add(element)
    return s

# remove element from set
def remove_el(s, el):
    s.remove(el)
    # s.discard(el)
    return s

# check element is present or not
def is_present(s, el):
    return el in s

# set union
def set_union(s1, s2):
    return s1.union(s2)

# set intersection
def set_intersection(s1, s2):
    return s1.intersection(s2)

# set difference
def set_difference(s1, s2):
    # return s1.difference(s2)
    return s1-s2

# set symmetric diffeence
def set_symmetric_diff(s1, s2):
    return s1.symmetric_difference(s2)

# check set is subset of another set or not
def check_is_subset(sub, main):
    return sub.issubset(main)

# disjoint

print(set1.isdisjoint(set2))

# clear  all element of a set
def clear_set(s):
    return s.clear()

# copy a set
def copy_set(s):
    return s.copy()

# remove arbitrary element
def remove_arbt_el(s):
    return s.pop()

# max and min in a set
def max_min(s):
    return max(s), min(s)

# update set element from another iterable
def update_set(s, itrable):
    s.update(itrable)
    return s

# create frozenset
fzset = frozenset([1,2,3,4])

# convert list to set
def list_to_set(list):
    return set(list)

# check two sets are equal
def is_equal(s1, s2):
    return s1==s2

# common (intersection) element between multiple sets
# s.intersection(s1,s2,s3)
# union between multiple sets (s.union(s1,s2,s3))