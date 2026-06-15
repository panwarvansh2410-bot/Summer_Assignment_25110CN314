arr = [1,2,3,4,5,8]
n = len(arr)
temp = []

for i in range(0,n):
    temp.append(arr[n-1-i])
print(arr, ": after reversing: ", temp)