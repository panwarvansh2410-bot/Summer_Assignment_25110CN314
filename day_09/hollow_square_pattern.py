m = int(input("enter no. rows : "))
n = int(input("enter no. columns : "))

for i in range(m):
    for j in range(n):
        if (i==0 or  j==n-1) or (j==0 or i==m-1):

            print("*",end="")
        else:
            print(" ",end="")

    print()