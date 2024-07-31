# static: only class level, not at instance level
#static method: method that belongs to a class rather than instance 

class Car:
    def __init__(self, brand, name):
        self.name = name
        self.brand = brand


    # static method
    @staticmethod
    def general_description():
        return f"cars are means of transport"
    
my_car = Car("mahindra", "xuv300")
print(Car.general_description())

    
