def perfect_num(n):
    n1 = n
    sum = 0
    for i in range(1,n):
        if n1%i==0:
            sum = sum+i

    if sum == n:
        return f'your number {n} is perfect number'
    else:
        return f'your number {n} is not a perfect number'


print(perfect_num(28))
   