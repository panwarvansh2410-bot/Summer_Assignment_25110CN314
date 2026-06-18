arr = [10, 20, 30, 40, 50, 60, 70]

find = 50
flag = 0
n = len(arr)
low =0
high = n-1
while low<=high:
    mid = int((low+high)/2)
    if arr[mid]==find:
        flag = 1
        break
    elif arr[mid]>find:
        high = mid-1
    else:
        low = mid+1
if flag==1:
    print(" succesfull searching element",find,"preent at position",mid+1)
else:
    print("unsuccessfull searching")        



