# check whether given number palindrome or not

num=int(input("Enter the number to check whether it is palindrome:"))
rev=0
i=num
while i > 0:
    digit = i % 10      # get last digit
    rev = rev * 10 + digit
    i = i // 10       # remove last digit

if num == rev:
    print(num,"is palindrome number")
else:
    print(num,"is not an palindrome number")