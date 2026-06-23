word = "Chitkara"
n = len(word)
temp2 = []
temp1 = []

for i in range(0,n):
    if word[i] not in temp1:
        temp1.append(word[i])

for j in range(0,len(temp1)):
    count = 0
    for k in range(0,n):
        if temp1[j]==word[k]:
            count+=1
    #print(temp[j],"--",count)
    temp2.append(count)

    max = 0
    for l in range(0,len(temp2)):
        if temp2[l]>max:
            max = temp2[l]

    if count == max:
        req = temp1[j]
print("most frequent element in string",word,"is :",req)                
               


