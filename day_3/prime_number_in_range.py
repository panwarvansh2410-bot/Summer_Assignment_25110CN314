num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))

for i in range (num1,num2+1):
    cout = 0
    for j in range(1,i+1):
        if i%j==0:

            cout+=1

            next = i
    if cout==2:
        print(next)
    
        
      

