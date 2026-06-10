r = 5
for i in range (r):
    for j in range(2*r-1):
        if (j>=i and j<=2*r-2-i) :
            print("*",end="")
        else:
                print(" ",end="")
    print()