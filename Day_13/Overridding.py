#Overridding in python

class A:
    def show(self):
        print("This is Class A")

class B(A):
    def show(self):
        print("This is Class B")

class C(A):
    pass


b1=B()
print(b1.show())        #overridding Class A show method

c1=C()
print(c1.show())        #calling the Class A show method


