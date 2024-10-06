nums = [0,1,0,3,12]
#1. brute approach
# for i in nums:
#     if i == 0:
#         nums.remove(i)
#         nums.append(i)
# print(nums)

#2. optimal solution
non_zero = 0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[non_zero],nums[i] = nums[i],nums[non_zero]
        non_zero+=1