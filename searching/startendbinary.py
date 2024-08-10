from jovian.pythondsa import evaluate_test_cases
def binarySearch(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi=mid-1
        else:
            lo=mid+1

def first_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid>0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binarySearch(0,len(nums)-1,condition)

def last_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] ==target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binarySearch(0,len(nums)-1,condition)
def first_last(nums, target):
    first = first_position(nums, target)
    if first == None:
        return (-1, -1)
    last = last_position(nums, target)
    return (first, last)

test_cases = [
    {"input": {'nums': [5, 7, 7, 8, 8, 10], 'target': 8}, "output": (3, 4)},
    {"input": {'nums': [5, 7, 7, 8, 8, 10], 'target': 7}, "output": (1, 2)},
    {"input": {'nums': [5, 7, 7, 8, 8, 10], 'target': 6}, "output": (-1, -1)},
    {"input": {'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'target': 1}, "output": (0, 0)},
    {"input": {'nums': [1, 1, 1, 1, 1, 1], 'target': 1}, "output": (0, 5)},
    {"input": {'nums': [], 'target': 3}, "output": (-1, -1)},
    {"input": {'nums': [2, 2, 2, 3, 3, 3, 3, 4, 4, 4], 'target': 3}, "output": (3, 6)}
]
evaluate_test_cases(first_last,test_cases)