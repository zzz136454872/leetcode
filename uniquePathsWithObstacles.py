from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid
        if len(grid)==0:
            return 1
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        count=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        count[0][0]=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    continue
                if i>0:
                    count[i][j]+=count[i-1][j]
                if j>0:
                    count[i][j]+=count[i][j-1]
        return count[-1][-1]

sl=Solution()
inp=[[0,0,0],[0,1,0],[0,0,0]]
print(sl.uniquePathsWithObstacles(inp))

