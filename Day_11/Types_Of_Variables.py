# Static variables and Class(static) Variables

class car:
    wheels=4

    def __init__(self):
        self.com="BMW"
        self.Mil="10"



c1=car()
c2=car()

c1.com="Audi"
car.wheels=6  #it will update the value for all the object

print(c1.com,c1.Mil,car.wheels) #we can call wheels variable(static variable) by using class name or object name as well
print(c2.com,c2.Mil,c2.wheels)