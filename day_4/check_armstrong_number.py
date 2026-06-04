num = int(input("enter a number : "))
num2 = num
digit = 0
num3=num

while num!=0:
    place =num%10
    digit+=1    #to count digits in the number
    num = int(num/10)


n = digit

sum =0
while num2!=0:
    term = num2%10
    num2 = int(num2/10)     
    sum = sum+term**n
    
if sum==num3:
    print("your entered number is an armstrong number")
else:
    print("your entered number is not an armstrong number")


