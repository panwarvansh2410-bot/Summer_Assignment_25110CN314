arr = [22,45,22,98,5,10]
large = arr[0]

for i in range(0,len(arr)):
    if arr[i]>large:
        large = arr[i]
        
sec_large = arr[0]

for j in range(0,len(arr)):
    if arr[j]>sec_large and arr[j]<large:
        sec_large = arr[j]

print("Second largest element is: ",sec_large)
print("Largest element is: ",large)
