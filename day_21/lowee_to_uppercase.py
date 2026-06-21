s = "hello"

result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)