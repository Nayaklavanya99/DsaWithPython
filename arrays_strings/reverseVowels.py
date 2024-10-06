input = "IceCreAm"

s = list(input)
nv = []
print(s)
vowels = ['a', 'e','i','o','u']
for i in s:
    if i.casefold() in ['a', 'e','i','o','u']:
        nv.append(i)
nv.reverse()
print(nv) 
for i in range(len(s)):
    if s[i].casefold() in ['a', 'e','i','o','u']:
        s[i] = nv.pop(0)
print(''.join(s))      
