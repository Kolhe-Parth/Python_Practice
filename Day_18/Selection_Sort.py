#select first element make it as min value compare it with all element change min if you get any smaller
# value the previous min after getting the min value swap it with first element continue this process

size=int(input("Enter the size of data:"))
list=[]

for i in range(size):
    data=int(input("Enter the data:"))
    list.append(data)


print("Unsorted data is:",list)

def sort(list,size):
    for i in range(size):
        min = i
        for j in range(i,size):
            if list[j] < list[min]:
                min=j

        temp=list[i]
        list[i]=list[min]
        list[min]=temp
    print("Sorted data is",list)


sort(list,size)









