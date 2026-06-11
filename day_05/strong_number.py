num = int(input("enter the number: "))
copy_of_num = num
sum = 0
while num != 0:
    place_value = num % 10
    num = int(num / 10)

    i = 0
    fact = 1

    while i < place_value:

        i += 1
        fact = fact * i

    sum = fact + sum
sum2 = sum

if sum2 == copy_of_num:
    print("your number", copy_of_num, "is Strong number")
else:
    print("your number", copy_of_num, "is NOT Strong number")
