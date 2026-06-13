def palindrome(num):
    num1 =num
    rev = 0
    while num1>0:
        digit=num1%10
        rev = rev*10+digit
        num1//=10
    if rev == num:
        return 'your number is palindrome'
    else:
        return ' not palindrome'

print(palindrome(1234))    

