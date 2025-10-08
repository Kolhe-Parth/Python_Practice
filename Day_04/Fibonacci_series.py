# first 50 fibonacci numbers  ---- num1=0   num2=1   series=0(num1)+1(num2)=1   1+1=2   1+2=3   2+3=5   3+5=8   5+8=13

num1=0
num2=1
print(num1,num2,end=" ")
series=num1+num2
while series < 50:

    print(series, end=" ")
    num1=num2
    num2=series
    series = num1 + num2


#Using Function
print("\n----------------Using function---------------------")
def fibonacci(n):
    a=0
    b=1


    if n==1:
        print(a,end='')
    else:
        print(a,b,end=' ')
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=' ')


num=int(input("Enter the number you want to print fibonacci numbers:"))

fibonacci(num)


