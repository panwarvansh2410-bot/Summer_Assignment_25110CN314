str1 = "Must watch Sapne vs Everyone"

i = 0
count = 0
max_len = 0

while i < len(str1):
    if str1[i] != " ":
        count += 1
        if count > max_len:
            max_len = count
    else:
        count = 0

    i += 1

print("Longest length =", max_len)