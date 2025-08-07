nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
left = 0
max_length = 0
zero_count = 0

for right in range(len(nums)):
    # Increment zero count if the current number is 0
    if nums[right] == 0:
        zero_count += 1

    # If zero count exceeds k, shrink the window from the left
    while zero_count > k:
        if nums[left] == 0:
            zero_count -= 1
        left += 1

    # Update the maximum length of the window
    max_length = max(max_length, right - left + 1)
print(max_length)