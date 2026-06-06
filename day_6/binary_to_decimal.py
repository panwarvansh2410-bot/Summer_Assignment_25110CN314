bin = int(input("enter a binary no. : "))
i = 0
decimal = 0
bin1 = bin

while bin>0:
    digit = bin%10
    decimal = decimal+digit*(2**i)
    i+=1
    bin=bin//10
print("decimal conversion of binary number",bin1,"is",decimal)


