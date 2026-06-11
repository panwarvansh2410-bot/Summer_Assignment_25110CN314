def factorial_of_num(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact*i
        i+=1
    print("factorial of number",num,"!","=",fact)

factorial_of_num(8)   