height = [1,1]
left ,right = 0,len(height)-1
max_area = 0
width,heiight = 0,0
while left < right:
    width = right - left
    heiight = min(height[left],height[right])
    area = width * heiight
    max_area = max(max_area,area)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(max_area)