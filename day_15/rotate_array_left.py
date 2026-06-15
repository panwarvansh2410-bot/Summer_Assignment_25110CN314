arr =[1,2,3,4,5,6,7]
k = int(input("Enter the number of place to rotate the array left: "))
n = len(arr)
temp =[]

arr1 = arr[:k]
arr2 = arr[k:n]
for i in range(0,len(arr2)):
    temp.append(arr2[i])

for j in range(0,len(arr1)):
    temp.append(arr1[j])

print(arr, ": after rotating left by ",k," places: ", temp)

