from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        flat = [num for row in grid for num in row]
        
        S_actual = sum(flat)
        S_set = sum(set(flat))
        S_expected = sum(range(1, n*n + 1))

        repeated = S_actual - S_set
        missing = S_expected - S_set

        return [repeated, missing]
    
sol = Solution()
print(sol.findMissingAndRepeatedValues([[1, 2, 3], [4, 9, 6], [7, 8, 9]]))  # Output: [0, 10]