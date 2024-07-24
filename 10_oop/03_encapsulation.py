# define car class and encapsulate price attribute, make it private and provide a getter and setter method for it

# getter & setter method

class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.__price = price #__ will make private (accessable only in class not in instance)

    # getter 
    def get_price(self):
        return f"Price of this car is {self.__price}"
    
    # setter
    def set_price(self, value):
        self.__price = value
    

my_car = Car("rang rover", "discovery sport", "10k USD")

# print(my_car.__price) #Error: we can not access private variable directly outside class
print(my_car.get_price())

my_car.set_price("20k usd")

print(my_car.get_price())


