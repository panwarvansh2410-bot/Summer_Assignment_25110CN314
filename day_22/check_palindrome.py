s = 'NAMAK'
n = len(s)
flag = 0
for i in range(0,n):
    
    if s[n-1-i] == s[i]:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("Yes",s,"is Palindrome")
else:
    print("NO",s,"is not Palindrome")
