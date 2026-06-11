num = int(input("enter a number : "))
rev = 0
digit = 0
while num!=0:
    psi =num%10
    digit+=1
    num = int(num/10)

print(digit)    
