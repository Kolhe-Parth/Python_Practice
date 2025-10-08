#Array Using Numpy

from numpy import *

arr1=array([1,45,76,32,23])

arr2=arr1.copy()

arr3=arr1.view()    #view() will update the value in both the array

arr1[1]=7

print(arr1)
print(arr2)
print(arr3)

print(id(arr1))
print(id(arr2))
print(id(arr3))