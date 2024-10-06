s ="weallloveyou"
k = 7

# below is proper code but it exceeds time limit
# cur_sum = 0
# max_sum = cur_sum

# for x in range(0, len(s)-k):
#     # print(cur_sum)
#     cur_sum = sum(1 for x in range(x, x+k) if s[x] in "aeiou")
#     print("cur:  ",cur_sum)
#     max_sum = max(max_sum,cur_sum)
# print(max_sum)   

vowels =set("aeiou")
cur_sum = sum(1 for x in s[:k] if x in vowels)
max_sum = cur_sum

for i in range(k, len(s)):
    if s[i-k] in vowels:
        cur_sum -= 1
    if s[i] in vowels:
        cur_sum += 1
    max_sum = max(max_sum, cur_sum)
print(max_sum)