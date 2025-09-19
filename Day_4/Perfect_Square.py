# Print the perfect square numbers between 1-500


for i in range(1,501):  # 501 because it will go till -1
     square=i**2
     if square <= 500:
         print("Square of",i,"is:",square)