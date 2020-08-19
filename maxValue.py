from typing import *

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        log=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            log[i][0]=grid[i][0] +(log[i-1][0] if i>0 else 0) 
        for j in range(len(grid[0])):
            log[0][j]=grid[0][j] +(log[0][j-1] if j>0 else 0)
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                log[i][j]=max(log[i-1][j],log[i][j-1])+grid[i][j]
        print(grid)
        print(log)
        return log[-1][-1]

sl=Solution()
grid=[[1,2,5],[3,2,1]]
print(sl.maxValue(grid))

