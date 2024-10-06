nums = [20,100,10,12,5,13]
bools =False
for i in range(len(nums)-2):
    for j in range(len(nums)-2):
        print(nums[i],nums[j+1],nums[j+2])
        if ((nums[i] <= nums[j+1] ) and nums[j+1]<= nums[j+2]):
            bools = True
            break
        else:
            bools = False
    if (j == len(nums)):
        if(nums[i] == nums[j]):
            print("val =  ",j,nums[j])
print(bools)

# def recur(n):
#     if n==0 or n==1:
#         print("recur")
#         return n
#     return n*recur(n-1)
    
# print(recur(5))