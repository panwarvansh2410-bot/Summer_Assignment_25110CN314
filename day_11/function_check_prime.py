def prime_num_check(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print("your entered number",num,"is not a prime number")
                break
        else:
            print("your entered number",num,"is a prime number")

    else:
          print("your entered number",num,"is not a prime number")      
prime_num_check(1)    