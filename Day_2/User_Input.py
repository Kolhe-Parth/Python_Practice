#Finding the cube of user input

num=int(input("Enter the number to find the cube: "))
print("\nUsing Common method:-")
cube1=num ** 3
print("Cube of",num,"is:",cube1,'\n')#\n to get space between two line

print("Using Predefine function 'pow':- ")

cube2=pow(num,3)
print("Cube of",num,"is:",cube2)