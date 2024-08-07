l = ["java", 'python', 'c++']
d = "programming language"

dd = dict.fromkeys(l, d)
print(dd)

ddd = {1:2, 2:3}

# d4 = {**dd, **ddd}
dd.update(ddd)
print(dd)