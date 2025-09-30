#init method is used to initialize the variables act is constructors(java) in python
class computer:

    def __init__(self,CPU,RAM):
        self.cpu1=CPU
        self.ram1=RAM

    def config(self):
        print("Config is",self.cpu1,self.ram1)


com1=computer("i5",16) #pass value to the class
com2=computer("ryzen 3",8)


com1.config()   #calling the config method using com1 object
com2.config()