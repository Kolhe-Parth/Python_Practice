#single level,multi level, multiple inheritance

class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A):                     #Single level Inheritance
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature is 3")


class C(B):                     #Multi level Inheritance
    def feature5(self):
        print("This is feature 5")


class D:
    def feature6(self):
        print("This is feature 6")


class E(A,D):                 #Multiple Inheritance
    def feature7(self):
        print("This is feature 7")



e1=E()
e1.feature1()
e1.feature6()

c1=B()
c1.feature3()
c1.feature1()