class Car:
    # class variable
    total_car_created = 0

    # class constructor
    def __init__(self, brand, model): #self is like this keyword of java
        self.brand = brand
        self.model = model
        # self.total_car_created +=1
        Car.total_car_created +=1
    
    # our own methods
    def car_details(self):
        return f"This is {self.model} from {self.brand}"
    

my_car = Car("Tata", "Nexon")
my_car2 = Car("Mahindra", "Scorpio-N")

print(my_car.brand, my_car.model, "\n", my_car.car_details())
print(my_car2.brand, my_car2.model)
print(Car.total_car_created)