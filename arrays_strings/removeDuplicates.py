nums = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums) :
        nums= list(set(nums))
        #nums = list(nums)
        print(nums)
        return len(nums)
    
print(removeDuplicates(nums))