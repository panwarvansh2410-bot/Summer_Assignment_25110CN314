arr = [64, 25, 12, 22, 11]
small = arr[0]
for i in range(0, len(arr) - 1):

    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)
