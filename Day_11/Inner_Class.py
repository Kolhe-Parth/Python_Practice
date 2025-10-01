#Class inside class

class student:

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.lap=self.laptop() #creating object of laptop class inside outer class


    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.ram="8Gb"
            self.cpu="i5"

c1=student(10,20,30)
c2=student(30,28,39)

print(c1)

print(c1.avg())
print(c2.avg())

laptop=c1.laptop() #creating object of laptop class outside class


print(c1.lap.ram) #Calling the laptop object using object defind inside outer class
print(laptop.brand) #calling the laptop object using object defind outside the class






