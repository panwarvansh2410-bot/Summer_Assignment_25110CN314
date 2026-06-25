str1 = "apple"
str2 = "plane"
temp = []
for i in range(0, len(str1)):
    for j in range(0, len(str2)):
        if str1[i] == str2[j]:
            if str1[i] not in temp:
                temp.append(str1[i])
for k in range(0,len(temp)):
    print(temp[k],end=" ,")
