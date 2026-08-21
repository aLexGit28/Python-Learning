class Rectangle:
    
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Method to calculate area
    def area(self):
        return self.length * self.width
    
    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)


# Create an object
rectangle1 = Rectangle(10, 5)

# Call the methods
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())