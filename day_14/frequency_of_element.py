arr = [22,45,22,98,5,10,22,43,54,22,34,22,54,22]
req = 22
count = 0
for i in range (0,len(arr)):
    if req == arr[i]:
        count+=1
print(count)

