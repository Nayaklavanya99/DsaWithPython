grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(len(grid)-1)
def equalPairs(grid):
    count = 0
   
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i] == [grid[k][j] for k in range(len(grid))]:
                count += 1
                          
    print(count)
    return count
print(equalPairs(grid))