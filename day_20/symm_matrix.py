a = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
row = len(a)
col = len(a[0])
flag = 0

for i in range(0, row):
    for j in range(0, col):

        if a[i][j] == a[j][i]:
            flag = 1
            break
        else:
            flag = 0 
            break

if flag:
    print("symmetric matrix")
else:
    print("not symmetric matrix")
