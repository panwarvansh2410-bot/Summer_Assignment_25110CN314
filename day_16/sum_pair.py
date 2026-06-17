arr = [1,12,34,56,11,23,43]
sum = 23
n = len(arr)
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]+arr[j] == sum:
            print("those elements whose sum is",sum,"are",arr[i],arr[j])