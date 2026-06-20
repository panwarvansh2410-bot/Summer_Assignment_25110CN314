arr1  = [[1,2,3],[4,5,6],[8,9,0]]
arr2 = [[2,3,0],[4,0,5],[1,1,2]]
row = len(arr1)
col = len(arr2[0])
result = [[0 for _ in range(col)] for _ in range(row)]


for i in range(0,row):
    for j in range(0,col):
        sum  = 0
        for k in range(0,row):
            sum = sum+arr1[i][k]*arr2[k][j]
       # print(sum)
            result[i][j]=sum 
        print(result[i][j],end=" ")
    print()
        