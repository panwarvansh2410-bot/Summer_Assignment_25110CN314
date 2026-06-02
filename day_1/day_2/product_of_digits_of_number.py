num = int(input("Enter a number: "))
product = 1
while num>0:
    digit= num%10
    product = product*digit
    num = int(num/10)

print("product of digits in your number is",product)    

