num1=int(input('Enter the 1st number:'))
num2=int(input('Enter the 2nd number:'))
num3=int(input('Enter the 3rd number:'))

if num1 > num2 and num1 > num3 :
    print(num1,"is greatest")

elif num2 > num3 and num2 > num1:
    print(num2,"is greatest")

else:
     print(num3,"is greatest")

#2nd option
print("\n2nd option")
greatest=max(num1,num2,num3)
print(greatest,"is greatest")
