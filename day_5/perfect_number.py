num = int(input("enter a number : "))
copy_of_num = num
i = 0
sum = 0
while i < num - 1:
    i += 1
    if num % i == 0:
        # finding factors of the number and adding them
        sum = sum + i


if sum == copy_of_num:
    print(
        "your number ", copy_of_num, "is Perfect number")
     # if sum of factors =  that number then it is a perfect number
else:
    print("your number ", copy_of_num, "is not a Perfect number")
