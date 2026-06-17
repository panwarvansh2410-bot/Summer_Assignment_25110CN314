arr1 = [1, 2, 2, 3, 4, 4]
arr2 = [2, 2, 2, 4, 4]

temp = []
used = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j] and j not in used:
            temp.append(arr1[i])
            used.append(j)
            break

print(temp)