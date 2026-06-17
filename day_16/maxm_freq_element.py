arr = [22,45,22,98,5,10,22,43,54,22,34,22,54,22]
n = len(arr)
temp = []
for i in range (0,n):
    count = 1
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            count+=1
    temp.append(count)
#print(temp)
m = len(temp)

large = temp[0]
for k in range(0,m):
    if temp[k] > large:
        large = temp[k]
#print(large)
    
if count == large:
    print("Most frequent element is : ",arr[i])

for i in range (0,n):
    count = 1
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            count+=1
    if count == large:
        print("Most frequent element is : ",arr[i])