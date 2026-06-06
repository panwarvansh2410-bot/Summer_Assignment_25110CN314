x = int(input("enter a number : "))
n = int(input("enter a number that power you want for num : "))
result = 1
cout=0
while cout<n:
    result = result*x
    cout+=1

print(n,"th power of",x,"is",result)
