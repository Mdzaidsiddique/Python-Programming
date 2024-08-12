class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model  = model

    def get_model(self):
        return self.__model
    
    def set_model(self, value):
        self.__model = value

    def __str__(self, brand, model):
        return f"this is hte {model} from {brand}"
    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


