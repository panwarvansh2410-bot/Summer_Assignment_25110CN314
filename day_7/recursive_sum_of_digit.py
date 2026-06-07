def sum_digit(n):
    if n==0:
        return 0
    digit = n%10
    n = n//10
    return digit+sum_digit(n)
    
    

print(sum_digit(5493))