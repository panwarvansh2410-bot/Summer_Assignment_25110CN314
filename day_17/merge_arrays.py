arr1 = [1,2,2,3,4]
arr2 = [4,3,7,9,8,9,10]
temp =[]

for i in range(0,len(arr1)):
    temp.append(arr1[i])
for j in range(0,len(arr2)):
    temp.append(arr2[j])

print(temp)