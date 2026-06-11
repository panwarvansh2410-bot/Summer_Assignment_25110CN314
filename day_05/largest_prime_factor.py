num = int(input("enter a number : "))


for i in range (1,num+1):
    if num%i==0:
        factor = i
    count = 0
    for j in range(1,factor+1):
        if factor%j == 0:
            count+=1

    if count == 2:
           
        largest = j

print(largest)        
        