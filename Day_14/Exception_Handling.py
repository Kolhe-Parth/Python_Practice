# try:   except:   finally:

num1=int(input("Enter the number for divisor:"))
num2=int(input("Enter the number for as dividend:"))

try:
    ans=num1/num2
    print("Answer is:",ans)

except Exception as e:
    print(e)


finally:
    print("Resource closed")  #every time we open any resource(ex:file) we need to close the resource here
