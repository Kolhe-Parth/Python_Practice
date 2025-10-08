#Accessing,modifying & Creating new file


f=open("My_Data.txt","r")

f1=open("Copy.txt","a")  #search for exiting file if not present then create the new file with same name

data=f.read() # → It reads the entire file and moves the cursor to the end.
              # Then, if you want to read the file again, you just reset it using : f.seek(0)
print(data)
f1.write(data)

f.close()
f1.close()
