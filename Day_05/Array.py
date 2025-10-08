from array import *

vals=array('i',[1,20,45,32,2])


print("array before Reverse",vals)
vals.reverse()
print(vals)

vals.reverse()
for i in range(len(vals)):
    print(vals[i])

print()
for j in vals:
    print(j)