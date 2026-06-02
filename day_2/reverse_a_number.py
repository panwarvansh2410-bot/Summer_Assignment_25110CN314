num = int(input("enter a number : "))
rev = 0

while num!=0:
    psi =num%10
    rev = rev*10+psi
    num = int(num/10)
print("reverse of your entered number is",rev)