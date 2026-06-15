arr =[1,2,3,4,5,6,7]
k = int(input("Enter the number of place to rotate the array right: "))
n = len(arr)
temp =[]

arr1 = arr[:n-k]
arr2 = arr[n-k:n]

for i in range(0,len(arr2)):
    temp.append(arr2[i])
for j in range(0,len(arr1)):
    temp.append(arr1[j])

print(arr, ": after rotating right by ",k," places: ", temp)