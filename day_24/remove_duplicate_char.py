word = "aabbbbccdddeeeeee"
n = len(word)

temp = []
for i in range(0,n):
    if word[i] not in temp:
        temp.append(word[i])

for j in range(0,len(temp)):
    print(temp[j],end="")        