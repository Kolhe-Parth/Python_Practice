#Functions in python

list=[10,13,42,56,335,6,7,42,24]


list1=int(input("Enter the numbers to check even or odd:"))
print(list1)

def check(x):
    even=0
    odd=0
    for i in x:
        if i%2==0:
            even +=1
        else:
            odd+=1
    return even,odd


even,odd=check(list)

print("Count of even numbers are:{} and count of odd number are:{}".format(even,odd))