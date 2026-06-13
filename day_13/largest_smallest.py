arr = [22,45,22,98,5,10]
large = arr[0]
small = arr[0]
for i in range(0,len(arr)):
    
    if arr[i]>large:
        large = arr[i]

    if arr[i]<small:
        small = arr[i]

print("largest element in an array : ",large)
print("smallest element in an array : ",small)