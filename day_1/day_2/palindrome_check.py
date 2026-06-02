num = int(input("enter a number : "))
num1=num
rev = 0

while num1!=0:
    digit =num1%10
    rev = rev*10+digit
    num1 = int(num1/10)

if rev == num:
    print("your entered number",num,"is palindrome")
else:
    print("your entered number",num,"is not palindrome")