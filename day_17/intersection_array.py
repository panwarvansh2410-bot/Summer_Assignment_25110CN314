arr1 = [1, 2, 2, 3, 4,4]
arr2 = [2, 2, 2, 4, 4]
temp = []

for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i] == arr2[j]:
                if arr1[i] not in temp:
                    temp.append(arr1[i])
print(temp)                
