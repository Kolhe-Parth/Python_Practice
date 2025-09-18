#printing numbers from 1 to 100 and skipping the numbers that are divisible by 3 or 5



i=1

while i<=100:

    if i%5 !=0:
        if i%3 !=0:
            print(i)

    i=i+1


#other way
print("\n2nd Method")
x=1
while x<=100:
    if x%3 !=0 and x%5 !=0:  #true true = true ,true false =false
     print(x)

    x=x+1