# property decorator: marking propetries read only
class Car:
    def __init__(self, brand, model, fuel_type):

        self.__brand = brand #private
        self.__model = model #private
        self.fuel_type = fuel_type #public

    @property # Read only
    def brand(self):
        return self.__brand

    @property #Read only
    def model(self):
        return self.__model

my_car = Car("Tata", "Nexon", "Petrol")

my_car.fuel_type = "Diesel" # we can override fule_type
my_car.model = "Safari" # but we cant modify private attributes without setter

print(my_car.brand, my_car.model, my_car.fuel_type)



