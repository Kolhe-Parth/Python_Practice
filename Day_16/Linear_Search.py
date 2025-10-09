#Linear Search using different method

def search(list,key):
    i=0

    while i < len(list):
        if list[i]==key:
            return True
            break
        i+=1

    return False


size=int(input("Enter the size of data:"))

print("Enter the data in list:")
list=[]
for x in range(size) :
    data=int(input(f"Enter {x+1} element:"))
    list.append(data)

key=int(input("Enter the element to search in the data:"))

if search(list,key):
    print("Element found")

else:
    print("Element not found")