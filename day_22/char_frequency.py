word = "Character"
n = len(word)

temp = []
for i in range(0,n):
    if word[i] not in temp:
        temp.append(word[i])

for j in range(0,len(temp)):
    count = 0
    for k in range(0,n):
        if temp[j]==word[k]:
            count+=1
    print(temp[j],"--",count)            
            
