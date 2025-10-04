#Basic calculator




num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print("1. Add \n2. Subtract \n3. Multiply \n4. Divide")




def cal(num1,num2):
    opt = int(input("Choose the option to select operation-"))
    if opt==1:
        print(f"Addition of {num1} and {num2} is: {num1+num2}")

    elif opt==2:
        print("Substraction of {} and {} is: {}".format(num1,num2,num1-num2))

    elif opt==3:
        print("Multiplication of {} and {} is: {}".format(num1,num2,num1*num2))

    elif opt==4:
        print("Division of {} and {} is: {}".format(num1,num2,num1/num2))

    else:
        print("\n---------You enter the wrong input please enter again---------\n")
        cal(num1,num2)


cal(num1,num2)

print("")




