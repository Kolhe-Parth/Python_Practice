#    *****
#    *****
#    *****
#    *****


i=1
while i<=4:
    j=1
    while j<=6:
        print("*",end="")
        j=j+1
    print()
    i=i+1

print("----------------------------")

#      ******
#      *****
#      ****
#      ***
#      **
#      *

x=6

while x>0:
    y = 1
    while y<=x:
        print("*",end="")
        y=y+1
    print()
    x=x-1


print("----------------------------")

#           *
#          **
#         ***
#        ****
#       *****
#


p=1
row=5
while p<=row:

    space = row - p
    r = 0
    while r<space:
        print(" ",end="")
        r = r + 1

    q = 0
    while q<p:
        print("*",end="")
        q =q+1


    print()
    p=p+1