num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))

for i  in range (num1,num2+1):
    j = i
    k = j
    digit =0
    while i!=0:
        beta = i%10
        digit+=1    # finding digits in a number
        i = int(i/10)


    sum = 0
    while j!=0:
        gamma = j%10
        j = int(j/10)
        sum = sum+gamma**digit  # find sum of place value raising power digit

    
       
    if k == sum:    # check sum equal to original number 
        print("armstrong number from",num1,"to",num2,"is",k)
      
