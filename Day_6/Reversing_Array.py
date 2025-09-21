# Reversing array using python

from array import *

size=int(input("Enter the size of data:"))

vals=array('i',[])

for i in range(size):
    num=int(input("Enter the integer values in array:"))
    vals.append(num)


print(vals)

revarr=array('i',[])


for e in range(size-1,-1,-1):

      revarr.append(vals[e])

print(revarr)


