num = int(input("enter a number : "))
test = []
while num > 0:
    rem = num % 2
    num = num // 2

    test.append(rem)
test.reverse()
print(test)  # binary of your number
