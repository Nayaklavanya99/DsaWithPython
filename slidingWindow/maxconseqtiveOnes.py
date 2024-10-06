nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
cur_sum = sum(1 for x in nums[:k] if x==1)
max_sum = cur_sum
print(cur_sum)
for i in range(len(nums)):
    if nums[i] == 1 and nums[i+1] ==1:
        cur_sum += 1
    
    max_sum = max(max_sum, cur_sum)
print(max_sum)
