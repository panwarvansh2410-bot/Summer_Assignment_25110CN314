alphabet = []

alphabet.append('A')
alphabet.append('B')
alphabet.append('C')
alphabet.append('D')
alphabet.append('E')
alphabet.append('F')

r = len(alphabet)
for i in range(r):
    # Print leading spaces
    for j in range(r-1-i):
        print(" ", end="")
    
    # Print ascending part (1 to i+1)
    for k in range(i):
        print(alphabet[k], end="")
    
    # Print descending part (i to 1)
    for k in range(i,-1,-1):
        print(alphabet[k], end="")
    
    print()
