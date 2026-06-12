arr = [22,48,22,98,5,5,10,22,43,54,43,22,34,5,198]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
            duplicate = arr[i]

if count > 1:
        print(duplicate, end=" ")
        