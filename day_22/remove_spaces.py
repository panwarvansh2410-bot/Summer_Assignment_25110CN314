word = "Mi cro sof t"
n = len(word)
temp =[]

for i in range(0,n):
    if word[i]!=" ":
        temp.append(word[i])

for j in range(0,len(temp)):
    print(temp[j],end="")         
    