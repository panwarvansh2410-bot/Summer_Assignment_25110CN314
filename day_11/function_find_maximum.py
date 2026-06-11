def maximum(num1, num2, num3):
    largest = num1

    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    return largest
max = maximum(98,34,889)
print("The maximum number is:", max)