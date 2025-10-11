#compare each element with next element if i > i+1 swap then check i+1 > i+2 follow same
list=[]

def sort(list,len):
    for i in range(len-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

size=int(input("Enter the size of data:"))

for i in range(size):
    data=int(input("Enter the data:"))
    list.append(data)


print("Data before sorting:",list)

sort(list,size)
print("List after Sorting:",list)



