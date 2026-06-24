str1 = "waterbottle"
str2 = "erbottlewat"

n = len(str1)
temp = []

k = int(input("Enter rotation position: "))

test2 = str1[k:n]
test1 = str1[:k]

for i in range(len(test2)):
    temp.append(test2[i])

for j in range(len(test1)):
    temp.append(test1[j])

flag = 1

for p in range(n):
    if temp[p] != str2[p]:
        flag = 0
        break

if flag == 1:
    print("Yes, rotation")
else:
    print("No, not rotation")