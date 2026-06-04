num = int(input("enter a number : "))
first = 0
second = 1
n=0

alpha = [first,second]

while n<num-2:
    

    next = first+second
    alpha.append(next)

    first=second
    second=next
    n+=1

print(alpha[num-1]) 