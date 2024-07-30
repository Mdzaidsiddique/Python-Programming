# enumarate
# zip
l1 = [1,2,3]
l2 = [9,10,11]

dict = {l1[i]:l2[i] for i in range(len(l1))}
print(dict)
# operator overloading

# static attribute in class
class Car:
    # static attribute
    wheels = 4

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

print(Car.wheels)
c = Car('taisor', 'toyota')
print(c.wheels)
c.wheels = 5
print(c.wheels)
print(Car.wheels)


# MRO: Method resultion order

# regEx for decimal number

# PEP 
