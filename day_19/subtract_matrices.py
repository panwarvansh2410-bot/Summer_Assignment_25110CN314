arr  = [[1,2,3],[4,5,6],[8,9,0]]
row = len(arr)
col = len(arr[0])
sum=0

for i in range(0,row):
    for j in range(0,col):
        if j==i:
            sum = sum+arr[i][j]
print("Sum of diagnol element is :",sum )