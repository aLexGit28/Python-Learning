class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Creating an object of Car
car = Car("Toyota", "Fortuner")

# Calling parent class method
car.show_brand()

# Calling child class method
car.show_info()