str1 = "army"
str2 = "mary"
flag = 0
for i in range(0,len(str1)):
    if str1[i] in str2:
        flag = 1
    else:
        flag = 0
if flag == 1:
    print("both strings",str1,"and",str2,"are anagrams")    
else: 
    print("both strings",str1,"and",str2,"are NOT anagrams")   