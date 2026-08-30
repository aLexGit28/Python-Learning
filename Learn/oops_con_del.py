class Sample:#Class initialisation

  num=0#initialising to zero

  def __init__(self, var):#Function declaration
    Sample.num+=1#Incrementing
    self.var=var#Assigning the value of var
    print("The object value is = ", var)#print statement
    print("The value of class variable is= ", Sample.num)#print statement

  def __del__(self):#Function declaration
    Sample.num-=1#Decrementing
    print("Object with value %d is exit from the scope"%self.var)#Print statement

    
S1=Sample(15)#Calling class
S2=Sample(35)#Calling class
S3=Sample(45)#Calling class
del S1
del S2
del S3