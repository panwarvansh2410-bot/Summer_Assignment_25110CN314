num = int(input("enter a number : "))
test =[]
while num > 0:
    rem = num % 2
    num = num // 2
    test.append(rem)
test.reverse()
#print("binary conversion of the number is ", test,end="")

bits =test.count(1)
print(bits)
