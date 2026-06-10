r = int(input("Enter the number of rows: "))
for i in range (r):
    for j in range(2*r-1):
        if (j<=r+i-1 and j>=r-i-1) :
            print("*",end="")
        else:
                print(" ",end="")
    print()