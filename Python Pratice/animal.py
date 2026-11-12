class Animal:
#self --> refers to the current object
    def __init__(self,name): # constructor of the class
        self.name = name  # Attribute of the class
    # constructor gets invoked/called auy=tomatically when an object of class is created
    

    def sleep(self):  # Methods/Behaviour/functions of the class
        print(f'{self.name} likes sleep in the night/day')
        
    def eat(self):
        print(f'{self.name} likes to eat')
        
        
obj_seal = Animal('Seal')

obj_seal.eat()
obj_seal.sleep()