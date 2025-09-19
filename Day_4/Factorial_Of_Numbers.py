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

