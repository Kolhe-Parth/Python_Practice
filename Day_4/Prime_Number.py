# Check whether given number is prime or not

num=int(input("Enter the number to check whether it is prime or not:"))
i=2
flag=-1
if num > 0:
    flag = 0
    while i < num:   # use i*i <= num   reduce time complexity    because if num has a factor larger than √num, the smaller one would already be found earlier
        if num%i==0:
            flag=1
            break
        i +=1

if flag==0:
    print(num,"is prime")

else:
    print(num,"is not prime")

if flag==-1:
    print("Number is negative")


