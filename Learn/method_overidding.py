class A:
    def sayhi (self):
        print ("I an in A")

    def sayhello (self):
        print ("Hello from A")
        
class B(A):
    def sayhi (self):
        print ("I am in B")

ob = B()
ob. sayhi ()
ob.sayhello()

ob1 = A()
ob1.sayhi()