num = int(input("enter a number : "))

i = 0
print("factors of number are : ")
while i < num:
    i += 1
    if num % i == 0:
        # finding factors of the number
        print(i, end=" ")
