def reverse_num(n,rev =0):
    
    if n ==0:
        return rev
    digit = n%10
    n = n//10
    rev = rev*10 + digit
    
    return reverse_num(n,rev)


print(reverse_num(5493))