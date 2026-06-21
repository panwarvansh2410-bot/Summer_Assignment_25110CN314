s = "hello"
temp = []
for i in range(0,len(s)):
    temp.append(s[len(s)-1-i])
    print(temp[i],end="")