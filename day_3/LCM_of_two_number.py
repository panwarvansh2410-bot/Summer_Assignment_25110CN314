num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
max = max(num1,num2)

while True:
    if max%num1==0 and max%num2==0:
        print("LCM = ",max)
        break
    max+=1