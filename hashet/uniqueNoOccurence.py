arr = [1,2,2,1,1,3]

def uniqueNoOccurence(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    count1 = {}
    for i in count.values():
        if i in count1:
            return False
        else:
            count1[i] = 1
    return True
    
    
print(uniqueNoOccurence(arr))


# Another Approach
def uniqueOccurrences(arr):
    count = {}
    
    # Count occurrences of each element
    for num in arr:
        count[num] = count.get(num, 0) + 1  # Optimized dictionary update
    
    # Check if occurrences are unique
    return len(set(count.values())) == len(count.values())
print(uniqueOccurrences(arr))