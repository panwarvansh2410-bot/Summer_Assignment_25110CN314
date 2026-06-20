arr= [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
row = len(arr)
col = len(arr[0])


for i in range(0,row):
    sum = 0
    for j in range(0,col):
        sum = sum +arr[i][j]
    print(sum)    