arr = [[1, 2, 3], [4, 5, 6], [8, 9, 0]]
row = len(arr)
col = len(arr[0]) 

result = [[0 for _ in range(col)] for _ in range(row)]

for i in range(0,row):
    for j in range(0,col):
        result[i][j]=arr[j][i]
        print(result[i][j],end=" ")
    print()    
