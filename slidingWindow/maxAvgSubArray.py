nums = [1,12,-5,-6,50,3]
k = 4
i=0
cur_sum = sum(nums[:k])
max_sum = cur_sum
for i in range(k,len(nums)):
    print(nums[i] - nums[i-k])
    cur_sum += nums[i] - nums[i-k]
    
    max_sum = max(max_sum,cur_sum)
print(max_sum/k)

    
    