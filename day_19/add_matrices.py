arr1 = [[1, 2, 3], [4, 5, 6], [8, 9, 0]]
arr2 = [[2, 3, 0], [4, 0, 5], [1, 1, 2]]
row = len(arr1)
col = len(arr1[0]) 

result = [[0 for _ in range(col)] for _ in range(row)]


for i in range(0, row):

    for j in range(0, col):

        result[i][j] = arr1[i][j] + arr2[i][j]
        

        print(result[i][j], end=" ")
    print()
