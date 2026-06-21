s = "Entertainment"
vow = ['A','E','I','O','U','a','e','i','o','u']
count = 0
n = len(s)
for i in range(0,n):
    if s[i] not in vow:
        count+=1
        
else:
    print("number of vowels in string",s,"-----",n-count)
print("number of consonant in string",s,"-----",count)    
