arr = [22,48,22,98,5,5,10,22,43,54,43,22,34,5,198]
temp = []

for i in range(0,len(arr)):
    if arr[i] not in temp:
        temp.append(arr[i])

print(temp)