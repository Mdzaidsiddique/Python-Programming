import math
# return multiple value

def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2* math.pi * radius

    return area, circumference

a, c = circle_stats(6)

print("area is :",a, "and circumference is :", c)

