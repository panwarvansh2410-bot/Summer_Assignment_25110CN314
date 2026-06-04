num = int(input("enter a number : "))
first = 0
second = 1
n=0
print(first,second,end=" ")

while n<num-2:
    

    next = first+second
    print(next,end=" ")
    first=second
    second=next
    n+=1
    
