# taking properties and behaiviour from parent classes
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def car_details(self):
        return f"This is the {self.model} from {self.brand}"
    
    def fule_type(self):
        return f"fuel type of {self.model} is Petrol or Diesel"
    
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    

my_car = Car("Mahindra", "Thar 4x4")
my_electric_car = Electric_car("tesla", "Cybertruck", "816 V nominal")

print(my_car.car_details())
print(my_electric_car.car_details())
    
    
# isinstance()

print(isinstance(my_electric_car, Car)) #True
print(isinstance(my_electric_car, Electric_car)) #True
print(isinstance(my_car, Electric_car)) #False


# Multiple inheritance 
class Engine:
    def engine_info(self):
        return "Engine Info.."
    
class Battery:
    def battery_info(self):
        return "Battery Info.."
    
class Vehivle(Engine, Battery): #python supports multiple inheritance
    pass

tata_punch = Vehivle()

print(tata_punch.engine_info())
print(tata_punch.battery_info())

