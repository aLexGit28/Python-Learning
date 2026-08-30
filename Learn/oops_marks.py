class Student:

  mark1, mark2, mark3 = 45, 91, 71 #class variable

  def process(self):                              #class method
    sum = Student.mark1 + Student.mark2 + Student.mark3 #Calculate the sum by accessing the class variables
    avg = sum/3#calculates the average
    print("Total Marks = ", sum)#Prints the sum
    print("Average Marks = ", avg)#Prints the average
    return

    
S=Student()#Creating an object
S.process()#Calling the function