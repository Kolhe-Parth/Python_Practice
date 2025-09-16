# Swapping of two numbers using different methods

x=5
y=6

#1st Method this requires one extra variable
temp=x
print("X,Y Before Swapping",x,y)
x=y
y=temp
print("X,Y After Swapping Using 3rd variable",x,y)

#2nd Method this method also require 1 extra bit for calculation as 5,6 are 3 bit but addition 5+6=11 which is 4 bit

x=x+y
y=x-y
x=x-y

print("X,Y After Swapping Without using Third variable",x,y)

#3rd method this method will only use the 3 bit for operation

x=x^y
y=x^y
x=x^y

print("X,Y After swapping Without using Third variable",x,y)


#4th Method inbuild in python

x,y=y,x

print("Swapping of Numbers without using Third variable",x,y)
