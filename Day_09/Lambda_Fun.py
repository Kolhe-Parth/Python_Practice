#Lambda function in python



f=lambda a:a*a   #find square without writing the function
sq=f(2)
print("Square is ",sq)

#Finding even numbers using function

num=[12,24,33,45,55,45,44,32,56]

def even(n):
     return n%2==0

even_num=list(filter(even,num))
print(even_num)


#Same using lambda function

evens=list(filter(lambda i:i%2==0,num))  #using lambda we can directly define function and reduce the number of lines

print(evens)
