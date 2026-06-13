def fibonacci_series(upto_term):
    first = 0
    second = 1
    n=0
    print(first,second,end=" ")

    while n<upto_term-2:
    

        next = first+second
        print(next,end=" ")
        first=second
        second=next
        n+=1
    
fibonacci_series(5)    
