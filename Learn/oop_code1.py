# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        # Call the parent class constructor
        super().__init__(brand)

        # Additional attribute
        self.model = model

    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Create an object of the Car class
car1 = Car("Toyota", "Camry")

# Call both methods
car1.show_brand()
car1.show_info()