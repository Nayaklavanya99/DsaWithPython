nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

nums1 = list(set(nums1))
nums2 = list(set(nums2))

def checkDiff(nums1, nums2):
    
        answer1 = []
        answer2=[]
        for i in nums1:
            if i not in nums2:
                answer1.append(i)
        for j in nums2:
            if j not in nums1:
                answer2.append(j)
        return [answer1, answer2]
def checkanothermethod(nums1, nums2):
    return list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))
print(checkDiff(nums1, nums2))
print(checkanothermethod(nums1, nums2))