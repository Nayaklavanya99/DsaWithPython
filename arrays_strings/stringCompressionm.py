chars =["a"]
res = []
result = []
dict1 = {}
if len(chars) == 1:
    print(1)
else:
    
    for i in range(len(chars)):
        print(chars[i] in res)
        count= 0
        if chars[i] in res:
            for j in range(len(chars)):
                if(chars[i]==chars[j]):
                    count+=1
                
        else:
            res.append(chars[i])
            
        print("res: ",res)
        dict1[chars[i]] = count
    for i in dict1:
        result.append(i)
        result.append(str(dict1[i]))
print(result)