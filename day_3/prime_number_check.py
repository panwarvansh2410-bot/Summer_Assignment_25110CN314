num = int(input("enter a number : "))
cout= 0

for i in range(1,num+1):
    if num%i==0:
        cout+=1

if cout==2:
        print("prime")    

else:
        print("not prime")