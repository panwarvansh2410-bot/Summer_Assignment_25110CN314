def armstrong(num):
    num1 = num
    num2 = num
    digit = 0
    while num1>0:
        place= num1%10
        digit+=1
        num1//=10
    sum = 0
    while num2>0:
        term = num2%10
        num2//=10

        sum = sum+term**digit

    if sum == num:
        return 'your no. is armstrong'
    else:
        return 'Not Armstrong' 
    
print(armstrong(223))    
    