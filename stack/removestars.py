
s = "erase*****"
l =[]
for i in range(len(s)):
    if s[i] == '*':
        l.pop()
    else:
        l.append(s[i])
        
print(''.join(l))