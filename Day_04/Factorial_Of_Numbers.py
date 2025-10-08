# Find the factorial of given number

num=int(input("Enter the number to find the factorial:"))
i=num
fact=1

if num==0:
    print("Factorial of",num,"is:",fact)

elif num < 0:
    print("Number is negative")

else:
    while i > 1:
        fact=fact*i
        i = i - 1
    print("Factorial of",num,"is:",fact)




#Using Recursion


print("\n---------------Using Recursion-------------------")

a=int(input("Enter the number of which you want to find the factorial:"))

def fact(num):

    if num < 0:
        print("Number is negative")
        return None
    if num==0:
        return 1

    return num * fact(num-1)



result=fact(a)

print("Factorial of {} is: {}".format(a,result))

