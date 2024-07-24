class Person:
    def __init__(self, name, age, gen):
        self.name = name
        self.age = age
        self.gen = gen

    # def __str__(self):
    #     return f"name {self.name}, age {self.age} {self.gen}"
    
p1 = Person("zaid", 35, "male")

del p1.gen # delete properties
print(p1)

del p1 #delete object

