r = int(input("Enter the number of rows: "))
for i in range(r):
    # Print spaces
    for j in range(r-1-i):
        print(" ", end="")
    
    # Print ascending part (1 to i+1)
    for k in range(1, i+2):
        print(k, end="")
    
    # Print descending part (i to 1)
    for k in range(i,0,-1):
        print(k, end="")
    
    print()
