arr = [5,4,2,7,1]
max = arr[0]
n = len(arr)
temp =[]

for i in range(0,n):
    if arr[i]>max:
        max = arr[i]
        
for j in range(1,max+1):
    if j not in arr:
        temp.append(j)
print("Missing numbers are : ",temp)        
               
