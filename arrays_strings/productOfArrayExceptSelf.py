nums = [0,11,2,0]

def productExceptSelf(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    
    return result
print(productExceptSelf(nums))
# for i in nums:
#     mul=1
#     if any(i == 0 for j in nums):
#         for k in range(len(nums)):
#             mul *= nums[k]
#         break
#     for j in range(len(nums)):
            
#         if(i==nums[j]):
#             continue
#         mul *= nums[j]
#     res.append(mul)
    
# print(res)

# def check(nums):
#     count_zero = 0
#     res = [0]*len(nums)
#     print(res)
#     for i in range(len(nums)):
#         mul=1
#         if any(nums[i] == 0 for j in nums):
#             count_zero +=1
#             print(count_zero)
#             if (count_zero > 1):
#                 print(count_zero,"greater")
#                 return res[0]*len(nums)
#             else:
#                 for k in range(len(nums)):
#                     if(nums[i]==nums[k]):
#                         continue
#                     print(nums[k])
#                     mul *= nums[k]
#             res[i]=mul
#             continue
#         for j in range(len(nums)):
                
#             if(nums[i]==nums[j]):
#                 continue
#             mul *= nums[j]
#         res[i]=mul
#     return res
    
# print(check(nums))