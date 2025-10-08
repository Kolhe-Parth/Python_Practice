# Del operation in array using python

from array import *

size=int(input("Enter the size of data:"))

vals=array('i',[])

for i in range(size):
    num=int(input("Enter the integer values in:"))
    vals.append(num)


print(vals)

x=int(input("Enter the number you want to delete in data: "))

k=0
flag=0

for e in vals:
    if x==e:
        print("Number Found on index:",k)
        del vals[k]
        flag=1
        print("Data after deletion",vals)
        break

    k+=1
if flag==0:
    print("Number not found in the data")

