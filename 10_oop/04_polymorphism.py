# class polymorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fule_type(self):
        return f"Fule type of {self.model} is petrol or Diesel"
    
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):
        return f"Fule type of {self.model} is Electric Charge"


my_car = Car("Hundai", "Verna")
my_electric_car = Electric_car("Tata", "Punch.ev", "85kw")

print(my_car.fule_type())
print(my_electric_car.fule_type())


# Method Overriding
class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

def animal_sound(animal):
    print(animal.speak())

animal_sound(cat)

# Method overloading
def mathmatical_operation(x,y, z=None):
    if z is not None:
        return x+y+z
    else:
        return x+y

print(mathmatical_operation(2,3)) #5
print(mathmatical_operation(2,3,4)) #9 


# function polymorphism : len()
# len(list), len(tuple), len(dict), len(string)