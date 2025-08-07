nums = [2,1,-1]


for i in range(len(nums)):
    left_sum = sum(nums[:i])
    right_sum = sum(nums[i+1:])
    if left_sum == right_sum:
        print(i)
        
        
        
def pivotIndex( nums) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # Initialize left sum
        
        for i in range(len(nums)):
            # Check if left sum equals the right sum
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum += nums[i]  # Update left sum
        
        return -1 

print(pivotIndex(nums))