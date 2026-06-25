arr1 = [1,3,3,5]
arr2 = [2,3,4,5]
temp =[]

for i in range(0,len(arr1)):
    temp.append(arr1[i])
for j in range(0,len(arr2)):
    temp.append(arr2[j])

n = len(temp)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if temp[j] > temp[j+1]:
            temp1 = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = temp1
print(temp)        
