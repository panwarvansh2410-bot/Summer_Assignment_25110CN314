arr = [1,0,2,0,3,0,0,5]
found = 0
n = len(arr)
temp = []
for i in range(0,n):
    if arr[i]!=found:
        temp.append(arr[i])
#print(temp)

for j in range(0,n):
    if arr[j] == found:
        temp.append(arr[j])
print(arr,": after moving zeroes to end: ",temp)