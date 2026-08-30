class Sample:
  def __init__(self, n1, n2):
    self.n1=n1      #public data member/variable
    self.__n2=n2    #private data member/variable


  def display(self):
    print("Class variable 1 = ", self.n1)
    print("Class variable 2 = ", self.__n2)


S=Sample(12, 14)
S.display()
print("Value 1 = ", S.n1)
print("Value 2 = ", S.__n2)